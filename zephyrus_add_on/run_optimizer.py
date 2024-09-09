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

@click.command()
@click.argument('zephyrus_in_file',
                type=click.Path(exists=True, file_okay=True, dir_okay=False, writable=False, readable=True,
                                resolve_path=True))
@click.argument('binding_in_file',
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
@click.option('--dot-file',
              type=click.Path(exists=False, file_okay=True, dir_okay=False, writable=True, readable=True,
                              resolve_path=True),
              help='Output file in dot format for visualization purposes.')

def main(zephyrus_in_file,
         binding_in_file,
         output_file,
         keep,
         verbose,
         dot_file
         ):

    out_stream = sys.stdout
    if output_file: out_stream = open(output_file, "w")

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
    binding_out_file = output_file
    if not output_file:
        binding_out_file = get_new_temp_file('json')

    temp = sys.stdout
    sys.stdout = sys.stderr
    cmd = ['-o', binding_out_file]
    if dot_file: cmd += ['-d', dot_file]
    cmd += [zephyrus_in_file, binding_in_file]
    logging.debug("Running bind optimizer with options: " + unicode(cmd))
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
