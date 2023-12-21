'''
Crear la cuanta de tipo KING y de esa cuenta metemos el titular la cantidad y una bonificaicon de %.
getter y setter solo para bonificacion.
Obligatoriamente tienen que tener entre 18 y 25 años, creando el metodo titular valido.
Ademas de retirar dinero solo si el titular es valido.
Hay que usar __str__.
'''

class KING:
    def __init__(self, titular, bono, edad, cantidad = 0):
        self.__titular = titular
        self.__cantidad = cantidad
        self.__edad = edad
        self.__bono = bono
    
    def comprobarEdad(self):
        if self.__edad >= 18 and self.__edad <= 25:
            return True
        
    @property
    def getBono(self):
        return self.__bono
    
    @getBono.setter
    def setBono(self, porcentaje):
        self.__bono = porcentaje
        
    def __str__(self):
        if (self.comprobarEdad()):
            return f"{self.__titular} con {self.__edad} años, es miembro KING, cuenta con un salario de {self.__cantidad} € con un bono del {self.__bono}%"
        print("No tienes edad suficiente para abrir la cuenta, tienes que tener entre 18 y 25 años")
        
k = KING("David", 10, 18, 5000)
print(k)