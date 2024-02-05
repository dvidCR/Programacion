class Persona:
    
    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    
    def mayorEdad(self, edad):
        if edad >= 18:
            return True
        else:
            return False
        
    def validadorDNI(self, dni):
        letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        
        if len(dni) == 9:
            number = int(dni[7])
            position = number % 23
            
            if dni[8] == letras[position - 1]:
                return True
        return False
        
            
    @property
    def getNombre(self):
        return self.__nombre
    
    @property
    def getEdad(self):
        return self.__edad
    
    @property
    def getDni(self):
        return self.__dni
    
    @getNombre.setter
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    @getEdad.setter
    def setEdad(self, edad):
        if (self.mayorEdad(edad)):
            self.__edad = edad
        self.__edad = 0
        
    @getDni.setter
    def setDni(self, dni):
        if (self.validadorDNI(dni)):
            self.__dni = dni
        
    def __str__(self):
        return f"El nombre es: {self.__nombre}, tiene {self.__edad} años y su dni es el {self.__dni}"
    
p = Persona("David", 19, "02145678C")
print(p.getNombre)
print(p.getEdad)
print(p.getDni)

p.setNombre = "Daniel"

p.setEdad = 9

p.setDni = "02145678F"

print(p)