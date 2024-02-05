class Habilidad:
    
    def __init__(self, tajo, flecha, bomba_humo):
        self.tajo = tajo
        self.flecha = flecha
        self.bomba_humo = bomba_humo
        
    def ejecutar(self, personaje, habilidad):
        self.personaje = personaje
        self.habilidad = habilidad
        if self.habilidad == self.tajo: 
            print(f'{self.personaje + " pegó un tajo"}')
        elif self.habilidad == self.flecha:
            print(f'{self.personaje + " disparo una flecha"}')
        elif self.habilidad == self.bomba_humo:
            print(f'{self.personaje + " tiró una  bomba de humo para escapar del peligro"}' )

        
class Aventurero(Habilidad):
    
    def __init__(self, tipo, vida, daño):
        self.tipo = tipo
        self.vida = vida
        self.daño = daño
        
    def aventurero(self):
        self.tipo = "Aventurero"
        self.vida = 60
        self.daño = 40
        
    def habilidad(self, habilidad):
        self.hability = Habilidad().ejecutar(self.tipo, habilidad)
        
class Ladron(Habilidad):
    
    def __init__(self, tipo, vida, daño):
        self.tipo = tipo
        self.vida = vida
        self.daño = daño
        
    def ladron(self):
        self.tipo = "Ladron"
        self.vida = 40
        self.daño = 50
        
    def habilidad(self, habilidad):
        self.hability = Habilidad().ejecutar(self.tipo, habilidad)
        
def habilidad(pj, hability):
        pj.habilidad(hability)

print("1. Aventurero")
print("2. Ladron")
print("!!!Por favor escriba el nombre tal cual como aparece sin el número y punto¡¡¡")
print("\n")

personaje = input("Escoge un personaje: ")

print("1. Tajo")
print("2. Flecha")
print("3. Bomba de Humo")
print("!!!Por favor escriba el nombre tal cual como aparece sin el número y punto¡¡¡")
print("\n")

escoger = input("¿Que habilidad quieres usar?: ")

match escoger:
    
    case "Tajo":
        habilidad(personaje, "self.tajo")
        
    case "Flecha":
        habilidad(personaje, "self.flecha")
        
    case "Bomba de Humo":
        habilidad(personaje, "self.bomba_humo")