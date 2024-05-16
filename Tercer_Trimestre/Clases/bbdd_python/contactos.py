## CLASES DEL MODELO DE DATOS

class contacto():
    
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    
    @property
    def getNombre(self):
        return self.nombre
    
    @getNombre.setter
    def setNombre(self, nombre):
        self.nombre = nombre
        
    @property
    def getApellido(self):
        return self.apellido
    
    @getApellido.setter
    def setApellido(self, apellido):
        self.apellido = apellido
        
    @property
    def getEdad(self):
        return self.edad
    
    @getEdad.setter
    def setNombre(self, edad):
        self.edad = edad
    
    