class Libro:
    def __init__(self, titulo, autor, ano_de_publicacion, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.año = ano_de_publicacion
        self.paginas = num_paginas
        
    def infoLibro(self,libro):
        if(self.titulo == libro):
            print(str(self.titulo) + ", " + str(self.autor) + ", " + str(self.ano_de_publicacion) + ", " + str(self.num_paginas))
        else:
            print("Libro no encontrado")

piedra_filosofal = Libro("La Piedra Filosofal", "J.K Rowling", 1997, 256)
los_cinco = Libro("Los Cinco y el tesoro de la isla", "Enid Blyton", 1942, 160)
quijote = Libro("El ingenioso hidalgo don Quixote de la Mancha", "Miguel de Cervantes", 1605, 1560)