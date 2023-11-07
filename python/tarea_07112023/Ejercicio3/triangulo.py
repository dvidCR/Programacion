from forma import Forma

class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lador2, lado3):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lador2
        self.lado3 = lado3
        
    def areaTriangulo(self):
        self.base = input("Escribe la base del triángilo: ")
        self.altura = input("Escribe la altura del triángulo: ")
        area = self.base * self.altura / 2
        print(f'{"El área del triángulo es " + area}')
        
    def perimetroTriangulo(self):
        self.lado1 = input("Escribe un lado del triángilo: ")
        self.lado2 = input("Escribe otro lado del triángulo: ")
        self.lado3 = input("Y escribe otro lado del triángulo: ")
        perimetro = self.lado1 + self.lado2 + self.lado3
        print(f'{"El área del triángulo es " + perimetro}')