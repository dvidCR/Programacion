from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
class Circulo(FiguraGeometrica):
    
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        print(f"El área del circulo es: {3.14 * self.radio ** 2}")
        
    def perimetro(self):
        print(f"El perímetro del circulo es: {2 * 3.14 * self.radio}")
        
class Rectangulo(FiguraGeometrica):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        print(f"El área del rectangulo es: {self.base * self.altura}")
        
    def perimetro(self):
        print(f"El perímetro del circulo es: {2 * (self.base + self.altura)}")
        
class Triangulo(FiguraGeometrica):
        
    def area(self, base, altura):
        self.base = base
        self.altura = altura
        print(f"El área del rectangulo es: {self.base * self.altura / 2}")
        
    def perimetro(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(f"El perímetro del circulo es: {2 * (self.base + self.altura)}")
        
class menu:
    
    def __init__(self, forma):
        self.forma = forma
    
    def areaCirculo(self):
        print("\n")
        radio = int(input("Escribe el Radio: "))
        self.forma(radio).area()
        
    def areaRectangulo(self):
        print("\n")
        base = int(input("Escribe la Base: \n"))
        altura = int(input("Escribe la Altura"))
        self.forma(base, altura).area()
        
    def areaTriangulo(self):
        print("\n")
        x = int(input("Escribe la coordenada x: \n"))
        y = int(input("Escribe la corrdenada y: \n"))
        z = int(input("Escribe la coordenada z: "))
        self.forma(x, y, z).area()
        
    def perimetroCirculo(self):
        print("\n")
        radio = int(input("Escribe el Radio: "))
        self.forma(radio).perimetro()
        
    def perimetroRectangulo(self):
        print("\n")
        base = int(input("Escribe la Base: \n"))
        altura = int(input("Escribe la Altura: "))
        self.forma(base, altura).perimetro()
        
    def perimetroTriangulo(self):
        print("\n")
        base = int(input("Escribe la Base: \n"))
        altura = int(input("Escribe la Altura: "))
        self.forma(base, altura).perimetro()
    
    
print("\n")
print("1. Circulo")
print("2. Rectangulo")
print("3. Triangulo")

p = int(input("Que quieres hacer(1, 2, 3): "))

match p:
    case 1:
        forma = Circulo
        print("\n")
        print("1. Área")
        print("2. Perímetro")
        
        c = int(input("Que quieres calcular(1, 2): "))
        
        if c == 1:
            menu(forma).areaCirculo()
        elif c == 2:
            menu(forma).perimetroCirculo()
            
    case 2:
        forma = Rectangulo
        print("\n")
        print("1. Área")
        print("2. Perímetro")
        
        r = int(input("Que quieres calcular(1, 2): "))
        
        if r == 1:
            menu(forma).areaRectangulo()
        elif r == 2:
            menu(forma).perimetroRectangulo()
            
    case 3:
        forma = Triangulo
        print("\n")
        print("1. Área")
        print("2. Perímetro")
        
        c = int(input("Que quieres calcular(1, 2): "))
        
        if c == 1:
            menu(forma).areaTriangulo()
        elif c == 2:
            menu(forma).perimetroTriangulo()