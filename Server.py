from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import os


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    class MyFuncs:
        def create(self, path):
            return path

        def read(self, path):
            return path

        def write(self, path):
            return path

        def rename(self, path):
                return path

        def remove(self, path):
            return path

        def mkdir(self, path):
            return path

        def rmdir(self, path):
            return path

        def readdir(self, path):
            return path


    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()
