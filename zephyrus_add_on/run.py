"This programs is a wrapper that allows to run zephyrus and the binding optimizer in sequential order"
__author__ = "Jacopo Mauro"
__copyright__ = "Copyright 2017, Jacopo Mauro"
__license__ = "ISC"
__version__ = "0.1"
__maintainer__ = "Jacopo Mauro"
__email__ = "mauro.jacopo@gmail.com"
__status__ = "Prototype"

import click
import logging
import uuid
import os
import sys
import json
import zephyrus2
import bindings_optimizer

__tmp_files = []

def get_new_temp_file(extension):
    global __tmp_files
    # probablility of picking up the same uuid is negligible
    name = os.path.join('/tmp', uuid.uuid4().hex + '.' + extension)
    __tmp_files.append(name)
    return name


def clean_temp_files():
    for f in __tmp_files:
        if os.path.exists(f):
            os.remove(f)


def read_json(json_file):
    json_data = open(json_file)
    data = json.load(json_data)
    json_data.close()
    return data

def extract_last_solution(inFile, outFile):
    """
    Extracts from a file the last solution saving it in another file.
    Rerturns true if a solutions is found.
    """
    solution = False
    sol = ""

    for line in reversed(open(inFile, 'r').readlines()):
        if not solution:
            if line.startswith("----------"):
                solution = True
        else:
            if line.startswith("----------"):
                break
            else:
                sol = line + sol

    with open(outFile, 'w') as f:
        f.write(sol)
    return solution


@click.command()
@click.argument('json_input_file',
                type=click.Path(exists=True, file_okay=True, dir_okay=False, writable=False, readable=True,
                                resolve_path=True))
@click.option('--output-file', '-o',
              type=click.Path(exists=False, file_okay=True, dir_okay=False, writable=True, readable=True,
                              resolve_path=True),
              help='Output file - Otherwise the output is printed on stdout.')
@click.option(
    '--keep', '-k',
    is_flag=True,
    help="Do not delete the intermediate files at the end of the execution.")
@click.option(
    '--verbose', '-v',
    count=True,
    help="Print debug messages.")
@click.option('--no-simmetry-breaking', is_flag=True,
              help="Deactivate the simmetry breaking constraint for Zephyrus.")
@click.option(
    '--solver',
    type=click.Choice(["lex-chuffed", "lex-gecode", "lex-or-tools", "lex-ortools","smt"]), default="lex-chuffed",
    help='Solver to use by Zephyrus.')
@click.option('--dot-file',
              type=click.Path(exists=False, file_okay=True, dir_okay=False, writable=True, readable=True,
                              resolve_path=True),
              help='Output file in dot format for visualization purposes.')
@click.option(
    '--run-only-zephyrus',
    is_flag=True,
    help="Run only zephryus, skip the binding optimizer.")


def main(json_input_file,
         output_file,
         keep,
         verbose,
         no_simmetry_breaking,
         solver,
         dot_file,
         run_only_zephyrus):

    out_stream = sys.stdout
    if output_file:
        out_stream = open(output_file, "w")

    if verbose != 0:
        if verbose == 1:
            logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.WARNING)
        elif verbose == 2:
            logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
        elif verbose >= 3:
            logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
        logging.warning("Verbose (" + str(verbose) + ") output.")
    else:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.ERROR)

    cmd = []
    zephyrus_out_file = get_new_temp_file('txt')
    if no_simmetry_breaking:
        cmd += ['--no-simmetry-breaking']
    cmd += ["-o", zephyrus_out_file, '-s', solver, json_input_file]

    logging.info("Running Zephyrus with options " + unicode(cmd))

    # run zephyrus redirecting stdout in stderr
    # to avoid in stdout error messages if the wrong version of antlr runtime is used
    temp = sys.stdout
    sys.stdout = sys.stderr
    zephyrus2.main(cmd)
    sys.stdout = temp

    logging.info("Exctracting last solution")
    binding_in_file = get_new_temp_file('json')
    if not extract_last_solution(zephyrus_out_file, binding_in_file): # no solution returned by zephryus
        json.dump({"error": "no_solution_found"}, out_stream)
    elif run_only_zephyrus: # do not run the binding optimizer
        json.dump(read_json(binding_in_file),out_stream)
    else:
        binding_out_file = output_file
        if not output_file:
            binding_out_file = get_new_temp_file('json')

        temp = sys.stdout
        sys.stdout = sys.stderr
        cmd = ['-o', binding_out_file]
        if dot_file:
            cmd += ['-d', dot_file]
        cmd += [json_input_file, binding_in_file]
        logging.info("Running bind optimizer with options: " + unicode(cmd))
        bindings_optimizer.main(cmd)
        sys.stdout = temp

        if not output_file:
            json.dump(read_json(binding_out_file), out_stream)

        # logging.debug("Binding optimizer solution")
        # bindings_opt_out =
        # logging.debug(json.dumps(binding_out_file, indent=1))

    if not keep:
        clean_temp_files()
    logging.info("Execution terminated correctly")

if __name__ == "__main__":
    main()
