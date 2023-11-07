from animal import Animal

class Gato(Animal):
    def __init__(self, maullar):
        self.maullar = maullar
    
    def maullo(self):
        self.nombre = "Mie"
        self.edad = "3 años"
        self.maullar = "Miau Miau *****"