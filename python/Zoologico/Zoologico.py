class Animal:
    def __init__(self,nombre,especie,alimentacion):
        self.nombre = nombre
        self.especie = especie
        self.alimentacion = alimentacion
    
    def Zoologico(self,animales):
        self.animales = []
        if (animales == mostrar):
            print(self.animales)
        if (animales == añadir):
            self.nombre = input("Que animal vas a añadir: ")
            self.especie = input("De que especie es: ")
            self.alimentacion = input("Cual va a ser si alimentacion: ")
            self.animales.append(self.nombre)
            self.animales.append(self.especie)
            self.animales.append(self.alimentacion)

leon = Animal("León", "Mamifero", "Carne")
delfin = Animal("Delfin", "Mamifero", "Arenque o Bacalao")