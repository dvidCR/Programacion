from persona import Persona

class Profesor(Persona):
   
    def __init__(self, numEmpleado):
        self.numEmpleado = numEmpleado
    
    def profesor(self):
        print(f'{"Nombre: " + self.nombre}')
        print(f'{"Edad: " + self.edad}')
        print(f'{"DNI: " + self.dni}')
        print(f'{"Número: " + self.numEmpleado}')