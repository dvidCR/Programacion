from forma import Forma

class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def areaRectangulo(self):
        self.base = input("Escribe la base del rectángulo: ")
        self.altura = input("Escribe la altura del rectángulo: ")
        area = self.base * self.altura
        print(f'{"El área del rectangulo es " + area}')
    
    def perimetroRectangulo(self):
        self.base = input("Escribe la base del rectángulo: ")
        self.altura = input("Escribe la altura del rectángulo: ")
        perimetro = 2 * (self.base + self.altura)
        print(f'{"El perímetro del rectangulo es " + perimetro}')