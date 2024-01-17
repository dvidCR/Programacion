'''
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def __str__(self):
        return f"El perro {self.nombre} es de raza {self.raza}."
    
    def __eq__(self, raza2): #Signinifia la comparación de 'equals'
        return self.raza == raza2.raza
    
perro = Perro("Melody", "Teckle")
print(perro.__str__())
perro2 = Perro("Gato", "Teckle")

if (perro == perro2):
    print("La raza de ambos perros es la misma")
else:
    print("La raza de ambos perros no es la misma")
'''

class Coche:
    def __init__(self, matricula, marca, modelo, caballos):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.caballos = caballos
    
    def __str__(self):
        return f"La marca es {self.marca} con la matricula {self.matricula} que es el modelo {self.modelo} con un total de {self.caballos} caballos de potencia."
    
    def __eq__(self, otroCoche): #Signinifia la comparación de 'equals'
        return self.marca == otroCoche.marca and self.modelo == otroCoche.modelo
    
    def __gt__(self, otroCoche): #Signinifia la comparación de 'mayor que'
        return self.caballos > otroCoche.caballos
    
    def __lt__(self, otroCoche): #Signinifia la comparación de 'menor que'
        return self.caballos < otroCoche.caballos
    
    def __add__(self, otroCoche): #Vale para añadir un objeto nuevo añadiendo cosas de otro objeto
        return Coche (self.matricula, self.modelo, self.modelo, self.caballos + otroCoche.caballos)
    
Coche1 = Coche("598589F", "Mercedes", "Benz", "150c")
print(Coche1.__str__())
Coche2 = Coche("981298D", "Volkswagen", "Cucaracha", "230C")
Coche3 = Coche1 + Coche2
print(Coche3.__str__())

if (Coche1 == Coche2):
    print("La marca y modelo son los mismos")
else:
    print("La marca, el modelo o ambos no son los mismos")
    
if (Coche1 > Coche2):
    print("El coche 1 es más rápido que el coche 2")
else:
    print("El coche 2 es más rápido que el coche 1")
    
if (Coche1 < Coche2):
    print("El coche 1 es más lento que el coche 2")
else:
    print("El coche 2 es más lento que el coche 1")