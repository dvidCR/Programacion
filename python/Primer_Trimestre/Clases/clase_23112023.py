from abc import ABC, abstractmethod

class Forma:
    
    def __init__(self, color, x, y, nombre):
        self.color = color
        self.x = x
        self.y = y
        self.nombre = nombre
        
    def imprimir (self):
        print (f"La forma tiene de x: {self.x} y de y:{self.y}, el color {self.color} y el nombre {self.nombre}")
    
    def getColor (self):
        return self.color
    
    def setColor (self,color):
        self.color = color
    
    def mover(self,x1,y1):
        self.x = x1
        self.y = y1
 
class Rectangulo (Forma):
    
    def __init__ (self,x,y, ladoMay, ladoMen):
        super().__init__("blanco", x, y, "rect")
        self.ladoMayor = ladoMay
        self.ladoMenor = ladoMen
        
    def imprimir(self):
        super().imprimir()
        print (f"Lado mayor: {self.ladoMayor} y lado menor: {self.ladoMenor}")
    
    
    def calcularArea (self):
        return self.ladoMayor * self.ladoMenor
    
    def calcularPerimetro(self):
        return 2 * self.ladoMayor + 2 * self.ladoMenor
    
    def mover (self, escalado):
        self.ladoMayor = self.ladoMayor * escalado
        self.ladoMenor = self.ladoMenor * escalado
        
class coche(ABC):
    
    @abstractmethod
    def __init__(slef):
        pass