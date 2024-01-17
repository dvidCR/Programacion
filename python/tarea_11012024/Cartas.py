class Carta:
    
    def __init__(self, carta):
        self.carta = carta
        
class Baraja:
    
    def __init__(self, *cartas):
        self.mazo = cartas
        
    def __str__(self):
        baraja = []
        for card in self.mazo:
            baraja.append(card.carta)
        return f"Las cartas mostradas en el mazo son {baraja}."
    
    def __len__(self):
        return len(self.mazo)
    
carta1 = Carta("Uno")
carta2 = Carta("Dos")
carta3 = Carta("Tres")
carta4 = Carta("Cuatro")
carta5 = Carta("Cinco")
carta6 = Carta("Seis")
carta7 = Carta("Sota")
carta8 = Carta("Caballo")
carta9 = Carta("Reina")
carta10 = Carta("Rey")
baraja = Baraja(carta1,carta2,carta3,carta4,carta5,carta6,carta7,carta8,carta9,carta10)

print(baraja)
print(len(baraja))