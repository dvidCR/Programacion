class Rueda:
    def __init__(self, diametro, fabricante):
        self.__diametro = diametro
        self.__fabricante = fabricante
        
    def girar(self):
        self.kilometros = 0
        
class Motor:
    def __init__(self, tipo, caballos):
        self.__tipo = tipo
        self.__caballos = caballos
        self.carburante = 800
        
    def inyectarCarburante(self):
        self.carburante-=1

class Coche:
    
    def __init__(self, color, velocidad, tamaño, ruedas, motor):
        self.__color = color
        self.__velocidad = velocidad
        self.__tamaño = tamaño
        self.__ruedas = ruedas
        self.__motor = motor
        
        
    def avanzar(self):
        cont = 0
        if Motor.carburante > 0:
            if cont < len(self.__ruedas):
                cont-=1
                for i in len(self.__ruedas):
                    Rueda[i].girar()
            Motor.inyectarCarburante()
            cont = 0
        else:
            print("Ya no te queda carburante")
            
    def __str__(self):
        ruedas_info = []
        for rueda in self.__ruedas:
            rueda = f"Rueda con diámetro {rueda._Rueda__diametro}, fabricante {rueda._Rueda__fabricante} y con un kilometraje de {Rueda.girar().kilometros}"
            ruedas_info.append(rueda)
        return f"Color: {self.__color}, Velocidad: {self.__velocidad}, Tamaño: {self.__tamaño}, {ruedas_info}, Motor de tipo {self.__motor._Motor__tipo} y con {self.__motor._Motor__caballos}."
            
if __name__ == '__main__':
    
    rueda1 = Rueda(20, "Michelin")
    rueda2 = Rueda(20, "Michelin")
    rueda3 = Rueda(22, "Michelin")
    rueda4 = Rueda(22, "Michelin")
    
    ruedas = [rueda1, rueda2, rueda3, rueda4]
    
    coche = Coche("rojo", 50, 2.3, ruedas, Motor("Diesel", 500))

    print(coche)
    
    coche.avanzar()