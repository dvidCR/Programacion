class Forma:
    def calcularArea(self):
        pass
    
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
        
    def calcularArea(self):
        print(3.14 * self.radio ** 2)
        
class Cuadrado(Forma):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2
    
    def calcularArea(self):
        print(self.lado1 * self.lado2)
        
def calcularArea(forma):
    forma.calcularArea()
    
print("\n")
print("--------------------------------------------------")
print("1. Área del Circulo")
print("2. Área del Cuadrado")
print("--------------------------------------------------")
print("\n")

calcular = input("Que quieres calcular: ")

match calcular:
    case "1":
        radio = int(input("Que radio tiene el circulo: "))
        calcularArea(Circulo(radio))
    
    case "2":
        lado1 = int(input("Cuanto mide el primer lado: "))
        lado2 = int(input("Cuanto mide el segundo lado: "))
        calcularArea(Cuadrado(lado1, lado2))