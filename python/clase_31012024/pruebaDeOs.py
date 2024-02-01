import os

'''print(os.listdir())
print(os.listdir(path='..'))

listar = os.listdir()
for i in range(len(listar)):
    print(listar[i])'''
    
ruta_app = os.getcwd()  # obtiene ruta del script 
contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir

for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    print(archivo)