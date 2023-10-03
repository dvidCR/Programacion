import random
contador = 0
listaAleatorio = []
listaOculta = []
ganador = False
enhorabuena = ""
fallos = [""]
#Son 54 palabras las que pueden salir para adivinar
palabrasAdivinar = ["gorila", "chimpance", "caballo", "ballena", "perro", "gato", "leon", "tigre", "elefante","jirafa", "delfin", "camello", "hipopotamo", "oso", "ornitorrinco","zorro", "rinoceronte", "guepardo", "raton", "hiena", "topo", "jaguar", "armario","balcon", "baño", "comedor", "habitacion", "despacho", "dormitorio", "espejo","fregadero", "horno", "microondas", "jardin", "lavabo", "lavadero", "lavaplatos","pasillo", "patio", "salon", "sotano", "techo", "bañera", "cama", "cocina", "cocina" ,"escalera" ,"lavadora" , "mesa" , "nevera", "puerta", "silla", "terraza", "ventana"]
#Escoge una palabra de la lista para que la adivinemos
palabraAleatoria = random.choice(palabrasAdivinar)
print(palabraAleatoria)

#Ponemos una nueva variable para mostrar la palabra oculta con _
palabraOculta = "_" * len(palabraAleatoria)

#El cuero del monigote
def cabeza():
    if (contador >= 1):
        print(""+"O")
def brazo1():
    if (contador >= 2):
        print("[")
def cuerpo():
    if (contador >= 3):
        print(""+"|")
def brazo2():
    if (contador >= 4):
        print(""+""+"]")
def pierna1():
    if (contador >= 5):
        print("|")
def pierna2():
    if (contador >= 6):
        print(""+""+"|")

#La parte visual
def tablero():
    print("\n")
    cabeza()
    brazo1()
    cuerpo()
    brazo2()
    pierna1()
    pierna2()
    print("\n")
    print(fallos)
    print("\n")
    print(enhorabuena+palabraOculta)
    print("\n")

def cambioLista():
    for i in palabraAleatoria:
        listaAleatorio.append(i)
        print(listaAleatorio)
    for i in palabraOculta:
        listaOculta.append(i)

def comprobacionLetra(jugador):
    if (len(jugador) == 1):
        if (jugador == listaAleatorio):

    else:
        return False

tablero()
while(ganador == False):
    jugador = input("Pon una letra: ")
    comprobacion = comprobacionLetra(jugador)
    if (comprobacion == True):
        tablero()
    else:
        contador+=1
        fallos = jugador + ","
        tablero()
    if (palabraOculta == palabraAleatoria):
        enhorabuena = "Enhorbuena la palabra es "
        ganador = True
    if (contador == 6):
        print("Perdiste")
        ganador = True