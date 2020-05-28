import xmlrpc.client
rpc = xmlrpc.client.ServerProxy('http://localhost:8000')

print("Ingresa un comando. Los comandos permitidos son:")
print("CREATE / READ / WRITE / RENAME / REMOVE / MKDIR / RMDIR / READDIR")
opc = input()
print('Ingresa path')
path = input()
if opc == 'CREATE':
    rpc.create(path)
if opc == 'READ':
    print('Texto del archivo leido')
    print(rpc.read(path))
if opc == 'WRITE':
    print('Escriba')
    texto = input()
    rpc.write(path, texto)
if opc == 'RENAME':
    print('Ingrese nuevo nombre')
    new_name = input()
    rpc.rename(path, new_name)
if opc == 'REMOVE':
    rpc.remove(path)
if opc == 'MKDIR':
    rpc.mkdir(path)
if opc == 'RMDIR':
    rpc.rmdir(path)
if opc == 'READDIR':
    print('Lista de archivos')
    print(rpc.readdir(path))
