from abc import ABC, abstractmethod

class Unidad(ABC):
    
    def __init__(self, tipo, vida):
        self.tipo = tipo
        self.vida = vida
    
    @abstractmethod    
    def mover(self):
        pass
    
    @abstractmethod
    def atacar(self):
        pass
        
class Infanteria(Unidad):
    
    def __init__(self):
        self.tipo = "Infanteria"
        self.vida = 25
        
    def mover(self):
        self.movimiento = 20
        self.rango = 1
        
    def daño(self):
        self.atacar = 10

class Caballería(Unidad):
    
    def __init__(self):
        self.tipo = "Caballería"
        self.vida = 35
        
    def mover(self):
        self.movimiento = 40
        self.rango = 5
        
    def daño(self):
        self.atacar = 8
        
class Arquero(Unidad):
    
    def __init__(self):
        self.tipo = "Arquero"
        self.vida = 10
        
    def mover(self):
        self.movimiento = 10
        
    def daño(self):
        self.atacar = 25
        self.rango = 40