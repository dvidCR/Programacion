'''
fichero = open("./fichero_datos.txt", "r")

for i in fichero:
    cadena = i.split(",")
    print(cadena[2])
'''

class Persona:
    
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        
class Lista_Personas:
    
    def __init__(self):
        self.lista_personas = []
        
    def carga(self, fichero):

        for i in fichero:
            cadena = i.split(",")
            persona = Persona(cadena[0], cadena[1], cadena[2])
            self.lista_personas.append(persona)
            

fichero = open("./fichero_datos.txt", "r")
persona = Lista_Personas()
persona.carga(fichero)

for i in persona.lista_personas:
    print(i.nombre)