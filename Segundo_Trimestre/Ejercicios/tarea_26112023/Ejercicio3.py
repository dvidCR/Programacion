from abc import ABC, abstractmethod

class Vehiculo(ABC):
    
    @abstractmethod
    def arrancar(self):
        pass
    
    @abstractmethod
    def detener(self):
        pass
    
    @abstractmethod
    def tocarBocina(self):
        pass
    
class Coche(Vehiculo):
    
    def __init__(self, sonido):
        self.sonido = sonido
        
    def arrancar(self):
        print(self.sonido)
        
    def detener(self):
        print(self.sonido)
        
    def tocarBocina(self):
        print(self.sonido)
        
class Motocicleta(Vehiculo):
    
    def __init__(self, sonido):
        self.sonido = sonido
        
    def arrancar(self):
        print(self.sonido)
        
    def detener(self):
        print(self.sonido)
        
    def tocarBocina(self):
        print(self.sonido)
        
class Bicicleta(Vehiculo):
    
    def __init__(self, sonido):
        self.sonido = sonido
        
    def arrancar(self):
        print(self.sonido)
        
    def detener(self):
        print(self.sonido)
        
    def tocarBocina(self):
        print(self.sonido)
        
def sonido(vehiculo, modo, sonido):
    if modo == "arrancar":
        vehiculo(sonido).arrancar()
    elif modo == "detener":
        vehiculo(sonido).detener()
    elif modo == "tocarBocina":
        vehiculo(sonido).tocarBocina()
    
print("\n")
print("Coche")
print("Motocicleta")
print("Bicicleta")

p = input("Que vehiculo escoges: ")

print("\n")
print("Arrnacar")
print("Detener")
print("Tocar la bocina")

p2 = input("Que quieres hacer: ")

try:
    match p2:
        case "Arrancar":
            p2 = "arrancar"
            if p == "Coche":
                s = "BRUM BRUM"
            elif p == "Motociclete":
                s = "PAM PAM PAM PAM"
            elif p == "Bicicleta":
                s = "Clicck"
        
        case "Detener":
            p2 = "detener"
            if p == "Coche":
                s = "PIIIIIIIIIIIII"
            elif p == "Motociclete":
                s = "BRUUUuuuum"
            elif p == "Bicicleta":
                s = "piiiiiii"
            
        case "Tocar la bocina":
            p2 = "tocarBocina"  
            if p == "Coche":
                s = "PI PIIIIII"
            elif p == "Motociclete":
                s = "PI PIIIIII"
            elif p == "Bicicleta":
                s = "RING RING"
                         
except NameError as e:
    print(e)
    
try:
    match p:
        case "Coche":
            p = Coche
        
        case "Motocicleta":
            p = Motocicleta
            
        case "Bicicleta":
            p = Bicicleta
            
except NameError as e:
    print(e)
    
sonido(p, p2, s)