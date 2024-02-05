class Libro:
    
    def __init__(self, titulo, autor, añoPublicacion):
        self.titulo = titulo
        self.autor = autor
        self.año = añoPublicacion
        
    def __eq__(self, otroLibro):
        return self.titulo == otroLibro.titulo
    
    def __lt__(self, otroLibro):
        return self.titulo < otroLibro.titulo
    
libro1 = Libro("Harry Potter", "J.K", 1995)
libro2 = Libro("Harry Potter", "J.K", 1995)
#libro3 = Libro("Los tres cerditos", "Alguien", 1750)
#libro4 = Libro("La parca", "La Muerte", 50)

if (libro1 == libro2):
    print("El libro 1 es igual al 2")
else:
    print("El libro 2 no es igual al 1")

if (libro1 < libro2):
    print("El libro 1 es menor que el 2")
else:
    print("El libro 2 es mewnor que es 1")