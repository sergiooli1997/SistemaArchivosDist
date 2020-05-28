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
            try:
                final_path = os.path.join(start_path, path)
                fd = open(final_path, "w+")
                fd.write("\n")
                fd.close()
                print('Archivo creado')
            except OSError:
                print('No se pudo crear archivo')

        def read(self, path):
            try:
                final_path = os.path.join(start_path, path)
                fd = open(final_path, "r")
                contents = fd.read()
                print('Archivo leido')
                return contents
            except FileNotFoundError:
                print('No existe archivo solicitado')

        def write(self, path, texto):
            try:
                final_path = os.path.join(start_path, path)
                fd = open(final_path, "a+")
                fd.write(texto)
                fd.close()
                print('Se escribio en archivo')
            except FileNotFoundError:
                print('No existe archivo solicitado')

        def rename(self, path, new_name):
            try:
                final_path = os.path.join(start_path, path)
                dir = os.path.dirname(final_path)
                new_dir = os.path.join(dir, new_name)
                os.rename(final_path, new_dir)
                print('Se renombro archivo')
            except FileNotFoundError:
                print('No existe archivo solicitado')

        def remove(self, path):
            try:
                final_path = os.path.join(start_path, path)
                os.remove(final_path)
                print('Se elimino archivo')
            except FileNotFoundError:
                print('No existe archivo solicitado')

        def mkdir(self, path):
            try:
                final_path = os.path.join(start_path, path)
                os.mkdir(final_path, mode=0o777)
                print('Se creo directorio')
            except OSError:
                print('No se pudo crear directorio')

        def rmdir(self, path):
            try:
                final_path = os.path.join(start_path, path)
                os.rmdir(final_path)
                print('Se elimino directorio')
            except OSError:
                print('No se pudo eliminar directorio')

        def readdir(self, path):
            try:
                if path == '/':
                    ls = os.listdir(start_path)
                else:
                    final_path = os.path.join(start_path, path)
                    ls = os.listdir(final_path)
                print('Se listo directorio')
                return ls
            except OSError:
                print('Error en el directorio')


    server.register_instance(MyFuncs())

    # Run the server's main loop
    server.serve_forever()
