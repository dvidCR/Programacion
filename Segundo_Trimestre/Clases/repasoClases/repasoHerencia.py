class Figura:
    
    def __init__(self, r, b, a, l):
        self.radio = r
        self.base = b
        self.altura = a
        self.lado = l
        
class Circulo(Figura):
        
    def calcularArea(self):
        return 3.14 * self.radio ** 2
    
class Cuadrado(Figura):
        
    def calcularArea(self):
        return self.lado * self.lado
    
class Triangulo(Figura):
        
    def calcularArea(self):
        return self.base * self.altura / 2


print(Circulo(15, None, None, None).calcularArea())

print(Cuadrado(None, None, None, 50).calcularArea())

print(Triangulo(None, 25, 3, None).calcularArea())