from producto import Producto

class Libro(Producto):
    def __init__(self, autor):
        self.autor = autor
    
    def nombreLibro(self):
        self.nombre = "Harry Potter"
        self.precio = 14.99
        self.categoria = "Fantasia"
        self.autor = "J.K Rowling"