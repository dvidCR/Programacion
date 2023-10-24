class Calculadora:
    def __init__(self,sumar,restar,multiplicar,dividir):
        self.sumar = sumar
        self.restar = restar
        self.multiplicar = multiplicar
        self.dividir = dividir
    
    def suma(self,dato1,dato2):
        self.sumar = dato1 + dato2
        print(str(dato1) + " + " + str(dato2) + " = " + str(self.sumar))
    
    def resta(self,dato1,dato2):
        self.sumar = dato1 + dato2
        print(str(dato1) + " + " + str(dato2) + " = " + str(self.restar))
        
    def multiplicacion(self,dato1,dato2):
        self.sumar = dato1 + dato2
        print(str(dato1) + " + " + str(dato2) + " = " + str(self.multiplicar))
    
    def division(self,dato1,dato2):
        self.sumar = dato1 + dato2
        print(str(dato1) + " + " + str(dato2) + " = " + str(self.dividir))