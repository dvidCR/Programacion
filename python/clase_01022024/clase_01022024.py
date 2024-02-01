import os
from datetime import datetime

ruta_app = os.getcwd()  # obtiene ruta del script 
print (ruta_app)
contenido = os.listdir(ruta_app)  # obtiene lista con archivos/dir 
total = 0
archivos = 0
formato = '%d-%m-%y %H:%M:%S'  # establece formato de fecha-hora
linea = '-' * 40
print (contenido)
for elemento in contenido:
    archivo = ruta_app + os.sep + elemento
    print (os.path.isfile(archivo))
    #if not os.access(archivo, os.R_OK) and os.path.isfile(archivo):
    archivos += 1
    estado = os.stat(archivo)  # obtiene estado del archivo
    tamaño = estado.st_size  # obtiene de estado el tamaño 
    
    # Obtiene del estado fechas de último acceso/modificación
    # Como los valores de las fechas-horas vienen expresados
    # en segundos se convierten a tipo datetime. 
    
    ult_acceso = datetime.fromtimestamp(estado.st_atime)
    modificado = datetime.fromtimestamp(estado.st_mtime)
    
    # Se aplica el formato establecido de fecha y hora
    
    ult_acceso = ult_acceso.strftime(formato)
    modificado = modificado.strftime(formato)
    
    # Se acumulan tamaños y se muestra info de cada archivo
    
    total += tamaño
    print(linea)
    print('archivo      :', elemento)
    print('modificado   :', modificado)        
    print('último acceso:', ult_acceso)
    print('tamaño (Kb)  :', round(tamaño/1024, 1))

print(linea)
print('Núm. archivos:', archivos)
print('Total (kb)   :', round(total/1024, 1))