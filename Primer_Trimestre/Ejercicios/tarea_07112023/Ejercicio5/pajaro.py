from animal import Animal

class Pajaro(Animal):
    def __init__(self, pio):
        self.pio = pio
    
    def piar(self):
        self.nombre = "Pájaro"
        self.edad = "1 Año"
        self.pio = "Pio pio"