import xmlrpc.client
import datetime
s = xmlrpc.client.ServerProxy('http://localhost:8000')

print("Ingresa un comando. Los comandos permitidos son:")
print("CREATE")
print("READ y WRITE")
print("RENAME")
print("REMOVE")
print("MKDIR y RMDIR")
print("READDIR")
opc = input()
if opc == 'CREATE':
    print('CREATE')
if opc == 'READ':
    print('READ')
if opc == 'WRITE':
    print('WRITE')
if opc == 'RENAME':
    print('RENAME')
if opc == 'REMOVE':
    print('REMOVE')
if opc == 'MKDIR':
    print('MKDIR')
if opc == 'RMDIR':
    print('RMDIR')
if opc == 'READDIR':
    print('READDIR')