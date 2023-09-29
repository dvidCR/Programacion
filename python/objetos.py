class coche:
    def __init__(self,color,forma,ventanas,ruedas):
        self.color = color
        self.forma = forma
        self.ventanas = ventanas
        self.ruedas = ruedas
deportivo = coche("rojo","deportivo","tintadas","lisas")
utilitario = coche("gris","sedan","normales","pequeñas")

print(deportivo.color)