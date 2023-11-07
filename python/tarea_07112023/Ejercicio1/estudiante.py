from persona import Persona

class Estudiante(Persona):
    def __init__(self, matricula):
        self.matricula = matricula
    def informacion(self):
        print(f'{"Nombre: " + self.nombre}')
        print(f'{"Edad: " + self.edad}')
        print(f'{"DNI: " + self.dni}')
        print(f'{"Matrícula: " + self.matricula}')