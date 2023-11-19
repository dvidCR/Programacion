class Personaje:
    
    def __init__(self, nombre, vida, fuerza, defensa, mana, debilidad, proyectil):
        self.nombre = nombre
        self.vida = vida
        self.fuerza = fuerza
        self.defensa = defensa
        self.mana = mana
        self.debilidad = debilidad
        self.proyectil = proyectil
    
    def interaccion(self, talk, swap, fight):
        self.talk = talk
        self.swap = swap
        self.fight = fight
    
    def atacar(self, personaje, enemigo):
        self.personaje = personaje
        self.enemigo = enemigo
        print(f'{self.personaje + " ataca a " + self.enemigo}')
    
    def hablar(self, saludar, insultar):
        self.saludar = saludar
        self.insultar = insultar
        print(self.saludar)
        print(self.insultar)
        
class Guerrero(Personaje):
    
    def __init__(self):
        self.nombre = "Guerrero"
        self.vida = 20
        self.fuerza = 40
        self.defensa = 30
        self.mana = 0
        self.debilidad = "Rayo", "Proyectil"
        self.proyectil = "Espada"
    
    def habilidades(self, estocada, tajo, puñalada):
        self.estocada = estocada
        self.tajo = tajo
        self.puñalada = puñalada
        

class Mago(Personaje):
    
    def __init__(self):
        self.nombre = "Mago"
        self.vida = 20
        self.fuerza = 15
        self.defensa = 5
        self.mana = 150
        self.debilidad = "Fisico", "Proyectil"
        self.proyectil = "Bola de Fuego"
    
    def habilidades(self, bola_fuego, curacion, rayo):
        self.bola_fuego = bola_fuego
        self.curacion = curacion
        self.rayo = rayo
        
class Arquero(Personaje):
    
    def __init__(self):
        self.nombre = "Arquero"
        self.vida = 20
        self.fuerza = 25
        self.defensa = 15
        self.mana = 0
        self.debilidad = "Fisico", "Fuego"
        self.proyectil = "Flecha"
    
    def habilidades(self, daga, camuflaje, doble_tiro):
        self.daga = daga
        self.camuflaje = camuflaje
        self.doble_tiro = doble_tiro