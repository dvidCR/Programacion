class perro:
    def __init__(self,nombre,raza,altura):
        self.nombre = nombre
        self.raza = raza
        self.altura = altura
    def ladrar(self):
        print("¡¡¡guau guau negga!!!!")
        
setter = perro("rayo", "settter", 0.5)

setter.ladrar()