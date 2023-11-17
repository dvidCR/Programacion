from abc import ABC, abstractmethod

class GameObject(ABC):
    
    @abstractmethod
    def update(self):
        pass

class miJuego(GameObject):
    def __init__(self):
        pass
    
    def update(self):
        print("Actualiza el juego")

class Arma(ABC):
    @abstractmethod
    def __init__(self, daño, cargador, tipo):
        self.daño = daño
        self.cargador = cargador
        self.tipo = tipo
        
    def disparar(self):
        pass
    
class pistola(Arma):
    def __init__(self):
        self.daño = 9
        self.cargador = 6
        self.tipo = "Monotiro"
        
    def disparar(self, tiros):
        self.tiros = tiros
        while(self.tiros != 0):
            if self.cargador != 0:
                self.cargador-=1
                self.tiros-=1
                print("BANG")
            else:
                for i in range(1,4):
                    print(i)
                    self.cargador = 6
            
        

arma = pistola()

arma.disparar(15)