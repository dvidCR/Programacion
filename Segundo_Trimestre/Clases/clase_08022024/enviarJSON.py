import json
import os

try:
    os.getcwd("D:\Clase\Programacion\Segundo_Trimestre\Clases\clase_08022024")
except:
    os.chdir("D:\Clase\Programacion\Segundo_Trimestre\Clases\clase_08022024") 

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def to_dict(self):
        data = {}
        data["nombre"] = self.nombre
        data["apellido"] = self.apellido
        return data

A = Persona("Dario", "Arroyo")
B = Persona("Mario", "Serradilla")   
peeps = []
peeps.append(A.to_dict())
peeps.append(B.to_dict())

with open("data.json", "w") as outfile:
    json.dump(peeps, outfile)