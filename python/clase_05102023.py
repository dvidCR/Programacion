nombre = "Alfonso"
def saludo(nombre):
    nombre = nombre + "Dr.Flamenco!!!"
    print(f"!Hola, {nombre}")
    
saludo(nombre)
print ("-->" + nombre)

numeros = [1,2,3]
def ejemploLista(lista):
    numeros.append(4)
    print(numeros)

ejemploLista(numeros)
print(numeros)

def saludar(persona1,persona2):
    print("hola" +persona1+ "hola2" +persona2)
    
saludar("Ignacio","Javier")
saludar("Javier","Ignacio")