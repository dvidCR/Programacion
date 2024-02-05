fichero = open('ejemplo.txt')

def escribirFichero():
    fichero = open("datos_guardados.txt", 'w')
    fichero.write("Contenido a escribir")
    fichero.close()

def leerFichero(f):
    lista = f.readlines()
    nombre = lista[0]
    telefono = lista[1]
    nacimiento = lista[2]
    residencia = lista[3]
    print(f"La persona {nombre} con el número {telefono}, nació el {nacimiento} y vive en {residencia}")
    
leerFichero(fichero)
escribirFichero()

fichero.close()

with open('ejemplo.txt', 'r') as fichero:
   fichero.read()