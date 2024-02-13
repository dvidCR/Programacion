from abc import ABC, abstractmethod

class Persona:
    
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        
class Legislador(Persona, ABC):
    
    def __init__(self, nombre, apellidos, provincia, camara):
        super().__init__(nombre, apellidos)
        
        self.provincia = provincia
        self.camara = camara
        
    def provinciaRepresenta(self):
        return self.provincia
    
    @abstractmethod
    def getCamara(self):
        pass
    
class Diputado(Legislador):
    
    def __init__(self):
        pass
    
    def getCamara(self):
        print(f"{self.nombre} {self.camara}")
        
class Senador(Legislador):
    
    def __init__(self):
        pass
    
    def getCamara(self):
        print(f"{self.nombre} {self.camara}")