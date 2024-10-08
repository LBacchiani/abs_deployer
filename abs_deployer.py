"""
abs_deployer.py:

Usage: abs_deployer.py [<options>] <abs program files>
  Options:
    -o, --ofile <file>
      file where to save the output
    -v, --verbose
    -k, --keep
      keep temp files
    -s, --solver <solver>
      chose the solver to use for zephyrus. Choices are gecode, smt, ortools, or chuffed. Default gecode
    -p, --port <port>
        zephyrus container port (integer value)

It requires a container running zephyrus2, see https://bitbucket.org/jacopomauro/zephyrus2/src/master/

Scenarios names have to differ from DC names

The first abs file is the program containing all the resource cost annotations

Requirements:
  Python packages
   - toposort https://pypi.python.org/simple/topsort/

  The absfrontend.jar should be in CLASSPATH  
"""
__author__ = "Jacopo Mauro"
__copyright__ = "Copyright 2016, Jacopo Mauro"
__license__ = "ISC"
__version__ = "0.1"
__maintainer__ = "Jacopo Mauro"
__email__ = "mauro.jacopo@gmail.com"
__status__ = "Prototype"


import copy
import getopt
import json
import logging as log
import math
import os
# import signal
import sys
import uuid
from functools import reduce

import psutil
from antlr4 import *
from requests import post as requests_post

import ABS.abs_extractor as abs_extractor
import bind_preferences_translator
import code_generation
import decl_spec_lang.decl_spec_lang as decl_spec_lang
import settings

# DEVNULL = open(os.devnull, 'wb')

# List of the temp files.
# TMP_FILES = []

# List of the running solvers.
RUNNING_SOLVERS = []

# If KEEP, don't delete temporary files.
KEEP = False

VERBOSE = False

#log.basicConfig(filename='example.log',level=log.DEBUG)
#log.basicConfig(level=log.DEBUG)


def usage():
    """Print usage"""
    print(__doc__)


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // math.gcd(a, b)


def remove_dots(obj):
    """
    Keeps only the part of the string after the dot to a json object
    """
    if isinstance(obj, str):
        return obj.rsplit('.', 1)[-1]
    elif isinstance(obj, dict):
        new = {}
        for k in obj.keys():
            if isinstance(k, str):
                new[k.rsplit('.', 1)[-1]] = remove_dots(obj[k])
            else:
                new[k] = remove_dots(obj[k])
        return new
    elif isinstance(obj, list):
        return map(remove_dots, obj)
    else:
        return obj


def read_json(json_file):
    json_data = open(json_file)
    data = json.load(json_data)
    json_data.close()
    return data


def send_signal_proc(signal, proc):
    """
    Sends the specified signal to the process, and to all its children.
    """
    if proc.poll() is None:
        for p in proc.children(recursive=True):
            try:
                p.send_signal(signal)
            except psutil.NoSuchProcess:
                pass
        try:
            proc.send_signal(signal)
        except psutil.NoSuchProcess:
            pass


# def clean():
#     """
#     Utility for (possibly) cleaning temporary files and killing the solvers
#     processes at the end of the solving process (even when the termination is
#     forced externally).
#     """
#     global RUNNING_SOLVERS
#     for solver in RUNNING_SOLVERS:
#         send_signal_proc(signal.SIGKILL, solver)
#     # Possibly remove temporary files.
#     if not KEEP:
#         for f in TMP_FILES:
#             if os.path.exists(f):
#                 os.remove(f)


def get_abs_class_names(deploy_annotations):
    classes = {}
    for i in deploy_annotations:
        classes[i["class"]] = [j["name"] for j in i["scenarios"]]
    return classes


# def get_abs_names(data):
#   """Extract from the json generated parsing the ABS the names of the classes, resouces, and interfaces"""
#   classes = {}
#   resources = set([])
#   interfaces = set([])
#
#   for i in data["classes"]:
#     classes[i["name"]] = []
#     for j in i["activates"]:
#       if len(j["scenarios"]) == 0:
#         classes[i["name"]].append(settings.DEFAULT_SCENARIO_NAME)
#       else:
#         classes[i["name"]].append(j["scenarios"][0])
#
#       for k in j["cost"].keys():
#         resources.add(k)
#
#   for i in data["hierarchy"]:
#     for j in data["hierarchy"][i]:
#       interfaces.add(j)
#
#   return (classes,resources,interfaces)


def generate_zep_input_from_annotations(deploy_annotations, classes):
    """
    Generate the partial input for zephyrus starting from the json internal
    representation extracted from the abs program.
    Note that the names can not contain a '.' that in the specification language
    has its own meaning
    """

    zep = {
        "components": {},
        "locations": {}
    }

    for i in deploy_annotations:
        component_name = i["class"]
        for j in i["scenarios"]:
            comp = {
                "provides": [{}],
                "requires": {},
                "resources": {}}

            # handle provide-ports
            comp["provides"][0]["ports"] = classes[component_name]
            comp["provides"][0]["num"] = j["provide"]

            # handle require-ports
            for k in j["sig"]:
                if k["kind"] == "require":
                    comp["requires"][k["type"]] = 1
                elif k["kind"] == "list":
                    comp["requires"][k["type"]] = k["num"]

            # handle resources
            comp["resources"].update(j["cost"])

            # decide the name
            name = j["name"] + settings.SEPARATOR + component_name

            zep["components"][name] = comp
    return zep


def initialDC(annotation):
    """
    Creates a new type of DC for every initially available DC
    It takes the annotation in json format.
    It returns the data to include in zephyrus input and the maps between the DC
    components and its real name
    """
    zep = {}
    dc_into_name = {}
    name_into_dc = {}

    for i in annotation["DC"]:
        name = settings.SEPARATOR + uuid.uuid4().hex
        zep[name] = {}
        zep[name]["num"] = 1
        zep[name]["cost"] = 0
        zep[name]["resources"] = {}
        for j in i.keys():
            if j != "name":
                zep[name]["resources"][j] = i[j]

        dc_into_name[(name,0)] = i["name"]
        name_into_dc[i["name"]] = (name, 0)

    return zep, dc_into_name, name_into_dc


def replace_default_cloud_provider_DC(data, smart_annotation):
    """
    Rewrites the number of DC if the users does not want to use the
    DEFAULT_NUMBER_OF_DC
    """
    if "cloud_provider_DC_availability" in smart_annotation:
        for i in smart_annotation["cloud_provider_DC_availability"].keys():
            if i not in data["locations"]:
                log.critical("The DC " + i + " defined in the smart annotation has not been found")
                log.critical("Exiting")
                sys.exit(1)
            data["locations"][i]["num"] = smart_annotation["cloud_provider_DC_availability"][i]
            log.debug("Reset number of DC for " + i)

def initialObjects(annotation):
    """
    Creates a new type of obj for every initially available obj
    It takes the annotation in json format.
    It returns the data to include in zephyrus input and the maps between the obj
    and its real name
    """
    zep = {}
    obj_into_name = {}
    name_into_obj = {}

    for i in annotation["obj"]:
        name = settings.SEPARATOR + uuid.uuid4().hex
        zep[name] = {}
        for j in i.keys():
            zep[name]["provides"] = i["provides"]
            zep[name]["resources"] = { "initial_obj_resource" : 1}
        obj_into_name[name] = i["name"]
        name_into_obj[i["name"]] = name

    return zep, obj_into_name, name_into_obj


def add_fictional_bindings_with_initial_objects(obj_into_name, zep_last_conf):
    """
    this function modifies the final configuraiton to allow bindings with initial objects
    """
    for j in zep_last_conf["bindings"]:
        if (j["provider"] in obj_into_name) or (j["requirer"] in obj_into_name):
            j["num"] = 0
    return zep_last_conf


def allow_incoming_bindings_for_initial_objects(annotation, name_into_obj, zep):
    """
    this function inject a -1 as a requirer for the intial objects
    this allows the binder to add bindings also to the intial object
    :param annotation the intial json annotation
    :param name_into_obj the zephyrus json specification
    :param: zep the initial zephyrus json specification
    :return: the modified zephyrus json specification
    """
    for i in annotation["obj"]:
        if "methods" in i:
            comp = zep["components"][name_into_obj[i["name"]]]
            comp["requires"] = {}
            for j in i["methods"]:
                # set value to -1 to allow the possible income of non mandatory bindings
                comp["requires"][j["add"]["param_type"]] = -1
    return zep


def allow_more_bindings_for_list_parameters(deploy_annotations, zep):
    """
    this function inject a -1 as a requirer for the objects having as input paramter a list
    this allows the binder to add more than required number of bindings
    :param deploy_annotations: the intial json annotation
    :param zep: the zephyrus json specification
    :return: the zephyrus json specification
    """
    for i in deploy_annotations:
        for j in i["scenarios"]:
            name = j["name"] + settings.SEPARATOR + i["class"]
            for k in j["sig"]:
                if k["kind"] == "list":
                    zep["components"][name]["requires"][k["type"]] = -1
            for k in j["methods"]:
                if k["add"]["param_type"] not in zep["components"][name]["requires"]:
                    zep["components"][name]["requires"][k["add"]["param_type"]] = -1
    return zep


# def extract_last_solution(inFile, outFile):
#     """
#     Extracts from a file the last solution saving it in another file.
#     Rerturns true if a solutions is found.
#     """
#     solution = False
#     sol = ""
#
#     for line in reversed(open(inFile,'r').readlines()):
#         if not solution:
#             if line.startswith("----------"):
#                 solution = True
#         else:
#             if line.startswith("----------"):
#                 break
#             else:
#                 sol = line + sol
#
#     with open(outFile, 'w') as f:
#         f.write(sol)
#     return solution


def main(argv):
    """
    Main procedure extracting the JSON file from the ABS code,
    calls Zephyrus, and
    generates the ABS code
    """
    output_file = ''
    zephyrus_solver = 'lex-chuffed'
    # dot_file_prefix = ''
    zephyrus_port = ''
    global KEEP

    try:
        opts, args = getopt.getopt(argv, "ho:vp:ks:", ["help", "ofile=", "verbose", "keep", "solver", "port="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-o", "--ofile"):
            output_file = arg
        elif opt in ("-k", "--keep"):
            KEEP = True
        elif opt in ("-v", "--verbose"):
            log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
            log.info("Verbose output.")
        elif opt in ("-s", "--solver"):
            if arg == 'chuffed':
                zephyrus_solver = 'lex-chuffed'
            elif arg == 'smt':
                zephyrus_solver = 'smt'
            elif arg == 'gecode':
                zephyrus_solver = 'lex-gecode'
            elif arg == 'ortools':
                zephyrus_solver = 'lex-or-tools'
            else:
                print("Solver {} not recognized".format(arg))
                usage()
                sys.exit(1)
        # elif opt in ('-d', '--dotfiles'):
        #    dot_file_prefix = arg
        elif opt in ('-p', '--port'):
            zephyrus_port = arg

    if len(args) < 1:
        print("1 argument is required")
        usage()
        sys.exit(1)

    if not zephyrus_port:
        print("Zephyrus port is required")
        usage()
        sys.exit(1)

    try:
        zephyrus_port = int(zephyrus_port)
    except ValueError:
        print("Zephyrus port must be an Int")
        sys.exit(1)

    input_files = [os.path.abspath(x) for x in args]
    out_stream = sys.stdout
    if output_file:
        out_stream = open(output_file, "w")

    # global TMP_FILES
    # pid = str(os.getpgid(0))
    # script_directory = os.path.dirname(os.path.realpath(__file__))

    log.info("Extract SmartDeployment, SmartDeployCloudProvider, SmartDeployCost  annotations and classes info")
    try:
        smart_dep_json, dc_json, deploy_annotations, module_name, classes, interfaces = abs_extractor.get_annotation_from_abs(input_files[0])
    except ValueError:
        log.critical("Parsing error in JSON smart deployment annotations")
        log.critical("Exiting")
        sys.exit(1)
    # uniform the cost of the Cloud instances
    payment_interval = [dc_json[i]["payment_interval"] for i in dc_json]
    mul = reduce(lcm, payment_interval, 1)
    for i in dc_json:
        dc_json[i]["cost"] = int(mul / dc_json[i]["payment_interval"] * dc_json[i]["cost"])
        dc_json[i]["payment_interval"] = mul

    # compute classes that have a Deploy annotation
    classes_names = [i["class"] for i in deploy_annotations]
    log.debug("Find SmartDeployCost annotation for classes " + str(classes_names))
    # remove classes that do not have a Deploy annotation
    for i in list(classes.keys()):
        if i not in classes_names:
            del(classes[i])

    if set(classes_names) != set(classes.keys()):
        log.critical("SmartDeployCost annotation and classes defined do not match: " + str(classes_names) + " differs from " + str(classes.keys()))
        log.critical("Exiting")
        sys.exit(1)

    if not classes_names:
        log.critical("No Deploy annotations found.")
        log.critical("Exiting")
        sys.exit(1)

    # compute the transitive closure of interfaces
    # main interface stays in the first position
    for i in classes.keys():
        to_process = set(classes[i])
        processed = set(classes[i])
        while to_process:
            interface = to_process.pop()
            if interface in interfaces:
                processed.update(interfaces[interface])
                to_process.update(interfaces[interface] - processed)
        classes[i] = list(classes[i]) + list(processed - set(classes[i]))

    # collect all the interface names
    interface_names = list(set(sum(classes.values(),[])))

    log.debug("DC json annotation")
    log.debug(json.dumps(dc_json, indent=1))

    log.debug("Smart deployment json annotation")
    log.debug(json.dumps(smart_dep_json, indent=1))

    log.info("Start generation of zephyrus json")

    initial_data = generate_zep_input_from_annotations(deploy_annotations,classes)
    #(interface_to_classes,class_to_interfaces) = code_generation.get_maps_interface_class(initial_data)

    log.info("Add location into zephyrus json")
    initial_data["locations"] = dc_json
    log.info("Add default location for deploying intial objects")
    initial_data["locations"].update(settings.DEFAULT_INITIAL_DC)

    log.debug("Zephyrus base file: " + json.dumps(initial_data))

    for i in smart_dep_json:
        log.info("Processing " + i["id"])
        data = {'locations': copy.deepcopy(initial_data['locations']),
                'components': copy.deepcopy(initial_data['components'])
                }

        log.info("Adding new DC")
        newDC, dc_into_name, name_into_dc = initialDC(i)
        data["locations"].update(newDC)

        log.info("Replace default number of DC if specified")
        replace_default_cloud_provider_DC(data,i)

        log.info("Adding new obj")
        newObj, obj_into_name, name_into_obj = initialObjects(i)
        data["components"].update(newObj)

        log.info("Parsing and adding specification")
        data["specification"] = decl_spec_lang.translate_specification(
            InputStream(i["specification"]),name_into_dc,
            name_into_obj,get_abs_class_names(deploy_annotations))

        log.info("Parsing and adding bind preferences")
        if "bind preferences" in i:
            data["bind preferences"] = list(map(lambda x: bind_preferences_translator.translate_preference(x, name_into_dc, name_into_obj, get_abs_class_names(deploy_annotations)), i["bind preferences"]))

        #######CHANGES FOR PORTED VERSION############
        log.debug("Zephyrus input")
        log.debug(json.dumps(data,indent=1))

        log.debug("Querying Zephyrus...")
        query_url = 'http://localhost:{}/process'.format(zephyrus_port)
        options = "--run-only-zephyrus,--solver," + zephyrus_solver
        zep_input = copy.deepcopy(data)
        if KEEP:
            options = '-k,' + options
        if VERBOSE:
            options = '--verbose,' + options
        zep_input['options'] = [x.strip() for x in options.split(',')]
        zep_last_conf = requests_post(query_url, data=json.dumps(zep_input)).json()
        if 'error' in zep_last_conf:
            log.critical("No solution found for " + i["id"] + "\nExiting")
            sys.exit(1)
        log.info("Extracting last solution")
        log.debug("Zephyrus last solution")
        log.debug(json.dumps(zep_last_conf, indent=1))

        log.debug("Querying Binding Optimizer...")
        options = ''
        if KEEP:
            options = '-k,' + options
        if VERBOSE:
            options = '--verbose,' + options
        query_url = 'http://localhost:{}/optimize'.format(int(zephyrus_port))
        zep_last_conf = add_fictional_bindings_with_initial_objects(obj_into_name, zep_last_conf)
        log.debug("Modified configuration for the binding optimizer")
        log.debug(json.dumps(zep_last_conf, indent=1))
        data = allow_incoming_bindings_for_initial_objects(i, name_into_obj, data)
        data = allow_more_bindings_for_list_parameters(deploy_annotations, data)
        to_send = {'zephyrus_in_file': data, 'binding_in_file': zep_last_conf}
        if options:
            to_send['options'] = [x.strip() for x in options.split(',')]
        opt_bindings = requests_post(query_url, data=json.dumps(to_send)).json()
        log.info("Extracting last solution")
        log.debug("Binding Optimizer last solution")
        log.debug(json.dumps(opt_bindings, indent=1))


        #######END CHANGES FOR PORTED VERSION############

        # zephyrus_in_file = "/tmp/" + pid + i["id"] + "_zep_input.json"
        # TMP_FILES.append(zephyrus_in_file)
        # with open(zephyrus_in_file, 'w') as f:
        #   json.dump(data,f,indent=1)
        #
        # log.info("Running Zephyrus")
        # zephyrus_out_file = "/tmp/" + pid + i["id"] + "_zep_output.txt"
        # TMP_FILES.append(zephyrus_out_file)
        # cmd = []
        # if KEEP:
        #   cmd += ['-k']
        #
        # # run zephyrus redirecting stdout in stderr
        # # to avoid in stdout error messages if the wrong version of antlr runtime is used
        # temp = sys.stdout
        # sys.stdout = sys.stderr
        # cmd += ["-o",zephyrus_out_file,'-s',zephyrus_solver, zephyrus_in_file]
        # zephyrus2.zephyrus2.main(cmd)
        # sys.stdout = temp
        #
        # log.info("Extracting last solution")
        # binding_in_file = "/tmp/" + pid + i["id"] + "_binding_in.json"
        # TMP_FILES.append(binding_in_file)
        # if not extract_last_solution(zephyrus_out_file,binding_in_file):
        #   log.critical("No solution found for " + i["id"])
        #   log.critical("Exiting")
        #   sys.exit(1)
        #
        # log.debug("Zephyrus last solution")
        # zep_last_conf = read_json(binding_in_file)
        # log.debug(json.dumps(zep_last_conf,indent=1))
        #
        # # reset the number of bindings with initial components (to allow the binder to decide the connections)
        # zep_last_conf = add_fictional_bindings_with_initial_objects(obj_into_name,zep_last_conf)
        # log.debug("Modified configuration for the binding optimizer")
        # log.debug(json.dumps(zep_last_conf, indent=1))
        # with open(binding_in_file, 'w') as f:
        #   f.write(json.dumps(zep_last_conf, indent=1))
        #
        # log.debug("Modified Zephyrus input for binding optimizer")
        # data = allow_incoming_bindings_for_initial_objects(i, name_into_obj, data)
        # data = allow_more_bindings_for_list_parameters(deploy_annotations, data)
        # log.debug(json.dumps(data,indent=1))
        # with open(zephyrus_in_file, 'w') as f:
        #   json.dump(data,f,indent=1)
        #
        #
        # log.info("Running bind optimizer")
        # binding_out_file = "/tmp/" + pid + i["id"] + "_binding_out.json"
        # TMP_FILES.append(binding_out_file)
        #
        # temp = sys.stdout
        # sys.stdout = sys.stderr
        # if dot_file_prefix:
        #   zephyrus2.bindings_optimizer.main(
        #     ["-o", binding_out_file, "-d", dot_file_prefix + i["id"] + ".dot", zephyrus_in_file, binding_in_file])
        # else:
        #   zephyrus2.bindings_optimizer.main(["-o",binding_out_file,zephyrus_in_file,binding_in_file])
        # sys.stdout = temp
        #
        # log.debug("Binding optimizer solution")
        # bindings_opt_out = read_json(binding_out_file)
        #
        # bindings_opt_out = bindings_opt_out["optimized_bindings"]
        # log.debug(json.dumps(binding_out_file,indent=1))

        log.info("Generating ABS code")
        code_generation.print_class(i,
                                    interface_names,
                                    zep_last_conf,
                                    opt_bindings["optimized_bindings"],
                                    deploy_annotations,
                                    classes,
                                    dc_into_name,
                                    obj_into_name,
                                    module_name,
                                    dc_json,
                                    out_stream)

    # log.info("Print code to add instances in CloudProvider")
    # code_generation.print_cloud_provider_modification(dc_json,out_stream)

    # log.info("Print producline info")
    # code_generation.print_productline(out_stream)
    # log.info("Clean.")
    # clean()
    log.info("Program Succesfully Ended")


if __name__ == "__main__":
    main(sys.argv[1:])