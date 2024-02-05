from abc import ABC, abstractmethod
import random

class Carta(ABC):
    
    @abstractmethod
    def mostrarInformacion(self):
        pass
    
class CartaDePoker(Carta):
    
    def __init__(self, poker):
        self.carta = poker
        
    def mostrarInformacion(self):
        print(self.carta)
        
class CartaMagica(Carta):
        
    def __init__(self, magica):
        self.carta = magica
        
    def mostrarInformacion(self):
        print(self.carta)
        
class CartaDeMostruo(Carta):
        
    def __init__(self, mosntruo):
        self.carta = mosntruo
        
    def mostrarInformacion(self):
        print(self.carta)


poker = [
    "2 de Picas", "3 de Picas", "4 de Picas", "5 de Picas", "6 de Picas", "7 de Picas", "8 de Picas", "9 de Picas", "10 de Picas", "Jota de Picas", "Reina de Picas", "Rey de Picas", "As de Picas",
    "2 de Corazones", "3 de Corazones", "4 de Corazones", "5 de Corazones", "6 de Corazones", "7 de Corazones", "8 de Corazones", "9 de Corazones", "10 de Corazones", "Jota de Corazones", "Reina de Corazones", "Rey de Corazones", "As de Corazones",
    "2 de Rombos", "3 de Rombos", "4 de Rombos", "5 de Rombos", "6 de Rombos", "7 de Rombos", "8 de Rombos", "9 de Rombos", "10 de Rombos", "Jota de Rombos", "Reina de Rombos", "Rey de Rombos", "As de Rombos",
    "2 de Tréboles", "3 de Tréboles", "4 de Tréboles", "5 de Tréboles", "6 de Tréboles", "7 de Tréboles", "8 de Tréboles", "9 de Tréboles", "10 de Tréboles", "Jota de Tréboles", "Reina de Tréboles", "Rey de Tréboles", "As de Tréboles"
]

magica = ["bola de fuego", "curar", "levantar muertos", "levitar objetos", "rayos"]
      
monstruo = ["Creeper", "Zombie", "Zombie Ahogado", "Mini Zombie", "Esqueleto", "Esqueleto de las nieves", "Araña", "Enderman", "Ender Dragon"]
       
print("\n 1. Carta de Poker \n 2. Carta Mágica \n 3. Carta de Monstruo")

p = int(input("Que carta quieres coger(1, 2, 3): "))

try:
    match p:
        case 1:
            r = random.choice(poker)
            CartaDePoker(r).mostrarInformacion()
        
        case 2:
            r = random.choice(magica)
            CartaMagica(r).mostrarInformacion()
            
        case 3:
            r = random.choice(monstruo)
            CartaDeMostruo(r).mostrarInformacion()
            
except NameError as e:
    print(e)