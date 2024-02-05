class Coche:
    def __init__(self,marca,modelo,color,kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = kilometraje
        
    def conducir(self,kilometros_conocidos):
        self.kilometraje = self.kilometraje + kilometros_conocidos
        print(str(self.marca) + ", " + str(self.modelo) + ", " + str(self.color) + ", " + str(self.kilometraje))