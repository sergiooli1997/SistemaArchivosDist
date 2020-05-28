from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os

start_path = 'C:/Users/giolo/PycharmProjects/SistemaArchivosDist'


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler, allow_none=True) as server:
    server.register_introspection_functions()


    class MyFuncs:
        def create(self, path):
            final_path = os.path.join(start_path, path)
            fd = open(final_path, "w+")
            fd.write("\n")
            fd.close()

        def read(self, path):
            final_path = os.path.join(start_path, path)
            fd = open(final_path, "r")
            contents = fd.read()
            return contents

        def write(self, path, texto):
            final_path = os.path.join(start_path, path)
            fd = open(final_path, "a+")
            fd.write(texto)
            fd.close()

        def rename(self, path, new_name):
            final_path = os.path.join(start_path, path)
            dir = os.path.dirname(final_path)
            new_dir = os.path.join(dir, new_name)
            os.rename(final_path, new_dir)

        def remove(self, path):
            final_path = os.path.join(start_path, path)
            os.remove(final_path)

        def mkdir(self, path):
            final_path = os.path.join(start_path, path)
            os.mkdir(final_path, mode=0o777)

        def rmdir(self, path):
            final_path = os.path.join(start_path, path)
            os.rmdir(final_path)

        def readdir(self, path):
            final_path = os.path.join(start_path, path)
            ls = os.listdir(final_path)
            return ls


    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()
