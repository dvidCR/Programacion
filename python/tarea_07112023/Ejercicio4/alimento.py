from producto import Producto

class Alimento(Producto):
    def __init__(self, fecha):
        self.fecha = fecha
        
    def caducidad(self):
        self.nombre = "palomitas"
        self.precio = 4.99
        self.categoria  = "Cualquiera"
        self.fecha = "Una semana"