from abc import ABC, abstractmethod

class Unidad(ABC):
    
    @abstractmethod
    
    def __init__(self, tipo, vida):
        self.tipo = tipo
        self.vida = vida
        
    def mover(self, movimiento):
        self.movimiento = movimiento
    
    def atacar(self, daño, rango):
        self.daño = daño
        self.rango = rango
        
class Infanteria(Unidad):
    
    def __init__(self):
        self.tipo = "Infanteria"
        self.vida = 25
        
    def mover(self):
        self.movimiento = 20
        self.rango = 1
        
    def daño(self):
        self.daño = 10

class Caballería(Unidad):
    
    def __init__(self):
        self.tipo = "Caballería"
        self.vida = 35
        
    def mover(self):
        self.movimiento = 40
        self.rango = 5
        
    def daño(self):
        self.daño = 8
        
class Arquero(Unidad):
    
    def __init__(self):
        self.tipo = "Arquero"
        self.vida = 10
        
    def mover(self):
        self.movimiento = 10
        
    def daño(self):
        self.daño = 25
        self.rango = 40