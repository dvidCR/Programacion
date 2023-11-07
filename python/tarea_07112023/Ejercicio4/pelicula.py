from producto import Producto

class Pelicula(Producto):
    def __init__(self, director):
        self.director = director
        
    def pelicula(self):
        self.nombre = "Harry Potter"
        self.precio = 6.99
        self.categoria = "Fantasia"
        self.director = "Alfonso Cuarón, Mike Newell, David Yates y Chris Columbus"