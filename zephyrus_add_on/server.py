"""
A simple HTTP server to call zephyrus.
Examples for sending requests:
    curl http://localhost:9001/health
    curl -F "mzn=@<FILE>" http://localhost:9001
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import urlparse
import logging
import tempfile
import os
import subprocess
import click
import json

# default timeout in seconds
TIMEOUT = 3600
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)


def remove_unicode(data):
    if isinstance(data, dict):
        return {remove_unicode(key): remove_unicode(value) for key, value in data.iteritems()}
    elif isinstance(data, list):
        return [remove_unicode(element) for element in data]
    elif isinstance(data, unicode):
        return data.encode('utf-8')
    else:
        return data

class MyServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_GET(self):
        '''
        Handle GET requests.
        '''
        logging.debug('GET %s' % (self.path))
        if urlparse.urlparse(self.path).path == "/health":
            self._set_headers()
            self.wfile.write("OK\n")
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        '''
        Handle POST requests.
        '''

        files = []
        try:
            logging.debug('POST %s' % (self.path))

            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            data = json.loads(self.data_string)


            logging.debug('Operation %s' % urlparse.urlparse(self.path).path)

            if urlparse.urlparse(self.path).path == "/process":

                file_id, name = tempfile.mkstemp(suffix='.json', text=True)
                os.write(file_id, self.data_string)
                os.close(file_id)
                files.append(name)

                timeout = unicode(TIMEOUT)
                if not "options" in data:
                    data["options"] = []

                cmd = ["timeout", timeout, "python", "run.py"] + data["options"] + [name]

                logging.debug('Running cmd {}'.format(cmd))
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate()
                if process.returncode != 0 and process.returncode != 124:
                    logging.debug("The command returned with return code {}. STDOUT <{}>. STDERR <{}>".format(
                        process.returncode, out, err))
                    raise ValueError("The command returned with return code {}. STDOUT <{}>. STDERR <{}>".format(
                        process.returncode, out, err))
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(out)

            elif urlparse.urlparse(self.path).path == "/optimize":

                zephyrus_in_file, zephyrus_in_file_name = tempfile.mkstemp(suffix='.json', text=True)
                with open(zephyrus_in_file_name, 'w') as f:
                    json.dump(remove_unicode(data['zephyrus_in_file']), f)
                files.append(zephyrus_in_file_name)

                binding_in_file, binding_in_file_name = tempfile.mkstemp(suffix='.json', text=True)
                with open(binding_in_file_name, 'w') as f:
                    json.dump(remove_unicode(data['binding_in_file']), f)
                files.append(binding_in_file_name)

                timeout = unicode(TIMEOUT)
                if not "options" in data:
                    data["options"] = []

                cmd = ["timeout", timeout, "python", "run_optimizer.py"] + data["options"] + [zephyrus_in_file_name, binding_in_file_name]

                logging.debug('Running cmd {}'.format(cmd))
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                out, err = process.communicate()
                if process.returncode != 0 and process.returncode != 124:
                    logging.debug("The command returned with return code {}. STDOUT <{}>. STDERR <{}>".format(
                        process.returncode, out, err))
                    raise ValueError("The command returned with return code {}. STDOUT <{}>. STDERR <{}>".format(
                        process.returncode, out, err))
                else:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/plain')
                    self.end_headers()
                    self.wfile.write(out)
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write("Operation {} not allowed".format(urlparse.urlparse(self.path).path))

        except ValueError as e:
            self.send_response(400)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("{}".format(e))
        # except Exception as e:
        #     self.send_response(400)
        #     self.send_header('Content-type', 'text/plain')
        #     self.end_headers()
        #     self.wfile.write("Detect genering excpetion: {}".format(e))
        finally:
            # delete files
            for i in files:
                if os.path.exists(i):
                    logging.debug("Removing file {}".format(i))
                    os.remove(i)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

def run(port=9001):
    server_address = ('', port)
    httpd = ThreadedHTTPServer(server_address, MyServer)
    print 'Starting httpd..., use <Ctrl-C> to stop'
    httpd.serve_forever()

@click.command()
@click.option('--port', '-p', type=click.INT, default=9001,
              help='Port used by the server to wait for requests.')
def main(port):
    run(port=port)

if __name__ == "__main__":
    main()