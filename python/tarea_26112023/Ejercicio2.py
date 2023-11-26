from abc import ABC, abstractmethod

class Empleado(ABC):
    
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        
    @abstractmethod
    def salario(self):
        pass

class EmpleadoPorHora(Empleado):
    
    def __init__(self, paga, horas):
        self.horas = horas
        self.paga = paga
    
    def salario(self):
        print(f"El salario neto es {self.paga - self.paga / self.horas}")
        print(f"El salario bruto es {self.paga - self.paga / self.horas - 2 / 100}")
        
class EmpleadoFijo(Empleado):
    
    def __init__(self, paga):
        self.paga = paga
        
    def salario(self):
        print(f"El salario netro es {self.paga}")
        print(f"El salario bruto es {self.paga - 2 / 100}")
        
print("\n")
print("///////////Calcular Salario\\\\\\\\\\")
print("1. Empleado por Horas")
print("2. Empleado Fijo")

p = int(input("Que salario vasa calcular(1, 2): "))

if p == 1:
    paga = int(input("Cuanto dinero cobra: "))
    horas = int(input("Cuantas horas a trabajado: "))

    EmpleadoPorHora(paga, horas).salario()
elif p == 2:
    paga = int(input("Cuanto dinero cobra: "))
    
    EmpleadoFijo(paga).salario()