from forma import Forma
import math

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        
    def circuloArea(self):
        self.radio = input("Escribe el radio del círculo: ")
        area = math.pi * self.radio ** 2
        print(f'{"El área del circulo es " + area}')
        
    def circuloPerimetro(self):
        self.radio = input("Escribe el radio del círculo: ")
        perimetro = 2 * math.pi * self.radio
        print(f'{"El área del circulo es " + perimetro}')