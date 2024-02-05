class Privado:
    
    def __init__(self, edad):
        self.__edad = edad
        
    @property
    def getEdad(self):
        return self.__edad
    
    @getEdad.setter
    def setEdad(self, edad):
        self.__edad = edad
    
    @getEdad.deleter    
    def deleteEdad(self):
        print("hola")
        del self.__edad
        
e = Privado(10)
e.setEdad = 30
print(e.getEdad)
del e.deleteEdad

class ejemplo:
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def __str__(self):
        return self.nombre + " " + self.apellido + " edad-->  " + str(self.edad)
    
e = ejemplo("David", "Casado", 19)
print(e)