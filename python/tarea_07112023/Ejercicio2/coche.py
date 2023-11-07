from vehiculo import Vehiculo

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo