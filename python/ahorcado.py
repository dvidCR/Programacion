import random
contador = 0
palabraOculta = ""
#Son 55 palabras las que pueden salir para adivinar
palabrasAdivinar = ["Gorila", "Chimpancé", "Caballo", "Ballena", "Perro", "Gato", "León", "Tigre", "Elefante","Jirafa", "Delfín", "Camello", "León marino", "Hipopótamo", "Oso polar", "Ornitorrinco","Zorro", "Rinoceronte", "Guepardo", "Ratón", "Hiena", "Topo", "Jaguar", "armario","balcón", "baño", "comedor", "habitación", "despacho", "dormitorio", "espejo","fregadero", "horno", "horno microondas", "jardín", "lavabo", "lavadero", "lavaplatos","pasillo", "patio", "salón", "sótano", "techo", "bañera", "cama", "cocina", "cocina" ,"escalera" ,"lavadora" , "mesa" , "nevera", "puerta", "silla", "terraza", "ventana"]
#Escoge una palabra de la lista para que la adivinemos
def escogerPalabra():
    palabrasAdivinar = random.choice(palabrasAdivinar)
    print(palabrasAdivinar)
#Ponemos una nueva variable para mostrar la palabra oculta con _
def ocultarPalabra(palabra):
    palabraOculta = "_" * len(palabra)
    print(palabraOculta)


