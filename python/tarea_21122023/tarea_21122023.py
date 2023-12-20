'''
Crea una clase que se cuenta bancaria, tiene los atributos titutal(pesona) y cantidad(€) de manera privada.
El titular es obligatorio pero la cantidad no.
Un contructor donde los datos esten vacios.
Con getter, setter y __str__.
Metodo extra Ingresar pero solo positivas y Retirar pero no puede quedar en número rojos.
'''

class Banco:
    
    def __init__(self, titular = None, cantidad = 0):
        self.__titular = titular
        self.__cantidad = cantidad
        
    def comprobarTitular(self):
        if self.__cantidad >= 0:
            if self.__titular == None:
                print("Para poder manejar el dinero de tu cuenta antes tiene que haber un titular")
                return False
                
        return True
    
    def comprobarNegativo(self):
        if self.__cantidad < 0:
            return False
        return True
    
    def ingresar(self, dinero):
        if (self.comprobarTitular()):
            if (self.comprobarNegativo()):
                self.__cantidad = self.__cantidad + dinero
        
    def retirar(self, dinero):
        if (self.comprobarTitular()):
            if (self.comprobarNegativo()):
                if self.__cantidad > dinero:
                    self.__cantidad = self.__cantidad - dinero
            print("No se puede retirar más saldo del que ya tienes")
      
    @property
    def getTitular(self):
        return self.__titular
    
    @property
    def getCantidad(self):
        return str(self.__cantidad) + " €"
    
    @getTitular.setter
    def setTitular(self, nombre):
        self.__titular = nombre
        
    @getCantidad.setter
    def setCantidad(self, cantidad):
        if (self.comprobarTitular()):
            if cantidad > 0:
                self.__cantidad = cantidad
            print("No se puede retirar más saldo del que ya tienes")
        
    def __str__(self):
        return f"El titular {self.__titular} tiene un saldo en la cuenta de {self.__cantidad}"
    
    
c = Banco()

print(c)

#c.setTitular = "David"
#c.setCantidad = 50
#print(c.getCantidad)

c.ingresar(50)
print(c.getCantidad)
c.setTitular = "Dario"
c.ingresar(50)
print(c.getCantidad)

c.retirar(100)
print(c.getCantidad)

c.retirar(25)
print(c)