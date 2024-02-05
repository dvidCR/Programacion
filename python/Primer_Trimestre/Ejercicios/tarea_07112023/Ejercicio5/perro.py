from animal import Animal
import random

class Perro(Animal):
    def __init__(self, ladrar, bufar):
        self.ladrar = ladrar
        self.bufar = bufar
        
    def ladrido(self):
        self.nombre = "Princesa"
        self.edad = "5 años"
        aleatorio = random.randint(0, 10)
        if(aleatorio <= 9):
            self.ladrar = "GUAUGUAUGUAU GUAUGUAU GUAUGUAUGUAUGUAU GUAU"
            print(f'{self.nombre + "/n" + self.edad + "/n" + self.ladrar}')
        else:
            self.bufar = "guf guf guf"
            print(f'{self.nombre + "/n" + self.edad + "/n" + self.bufar}')