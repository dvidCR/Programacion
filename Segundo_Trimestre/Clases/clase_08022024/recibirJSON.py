import json
import os

try:
    os.getcwd("D:\Clase\Programacion\Segundo_Trimestre\Clases\clase_08022024")
except:
    os.chdir("D:\Clase\Programacion\Segundo_Trimestre\Clases\clase_08022024")       

class Persona:
    
    def __init__(self, name, nickname):
        self.name = name
        self.nickname = nickname
        
    def mensaje(self):
        return f'La persona {self.name} {self.nickname} me ha mandado esto'

with open("data.json", "r") as openfile:
    data = json.loads(openfile.read())
    a = data[0]["nombre"], data[0]["apellido"]
    b = data[1]["nombre"], data[1]["apellido"]
    
p1 = Persona(a[0], a[1])
p2 = Persona(b[0], b[1])
print(p1.mensaje())
print(p2.mensaje())