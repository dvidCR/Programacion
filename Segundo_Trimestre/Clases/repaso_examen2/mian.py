'''
Escribir una función que pida un número entero entre 1 y 10
y guarda en un fichero con el nombre tabla-n.txt
la tabla de multiplicar de ese número,
donde n es el número introducido.
'''

import os

if (os.getcwd != "D:/Clase/Programacion/Segundo_Trimestre/Clases/repaso_examen2"):
    os.chdir("D:/Clase/Programacion/Segundo_Trimestre/Clases/repaso_examen2")

def tabla_mul(num):
    with open("./tabla-n.txt", "w+") as f:
        for i in range(0, 10):
            f.write(f"{num} * {i} = {num * i}\n")
    
    leer_tabla()

def leer_tabla():
    fichero = open("./tabla-n.txt", "r")
    print(fichero.read())
    fichero.close()
    
        
tabla_mul(9)