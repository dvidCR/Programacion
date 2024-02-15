from abc import ABC

class Puerta(ABC):
    
    def __init__(self):
        pass
    
    def abrir(self):
        pass
    
    def cerrar(self):
        pass
    
class puertaBloqueable(Puerta, ABC):
    
    def __init__(self):
        pass
    
    def bloquea(self):
        pass
    
    def desbloquea(self):
        pass
    
class Alarma(ABC):
    
    def __init__(self):
        pass
    
    def alarmaActivada(self):
        pass
    
    def activarAlarma(self):
        pass
    
    def desactivarAlarma(self):
        pass
    
class componenteDeCoche:
    
    def __init__(self, descripcion, peso, coste):
        self.descripcion = descripcion
        self.peso = peso
        self.coste = coste
        
    def __str__(self):
        return f"El componente {self.descripcion} pesa {self.peso} kilos y tiene un coste de {self.coste}€"
    
class puertaCoche(componenteDeCoche, puertaBloqueable, Alarma):
    
    def __init__(self, estaBloqueada):
        super().__init__(componenteDeCoche("puerta", 15, 60))
        self.__estaBloqueada = bool(estaBloqueada)
        
    def bloquea(self):
        return super().bloquea(self.__estaBloqueada)
    
    def desbloquea(self):
        return super().desbloquea(self.__estaBloqueada)
    
    def abrir(self):
        if (self.bloquea):
            return super().abrir(False)
        else:
            return super().abrir(True)
    
    def cerrar(self):
        if (self.abrir()):
            return super().cerrar(True)
        else:
            return super().cerrar(False)
        
    def activarAlarma(self):
        if (self.activarAlarma()):
            return super().activarAlarma(False)
        else:
            if (self.__estaBloqueada):
                return super().activarAlarma(True)
            
    def desactivarAlarma(self):
        if (self.alarmaActivada()):
            if (self.__estaBloqueada):
                return super().desactivarAlarma(True)
            else:
                return super().desactivarAlarma(False)
            
    def alarmaActivada(self):
        if (self.activarAlarma()):
            return super().alarmaActivada(True)
        elif (self.desactivarAlarma()):
            return super().alarmaActivada(False)
        
class Coche(componenteDeCoche):
    
    def __init__(self, componentes = 4, descripcion = "puerta", peso = 15, coste = 60):
        super().__init__(descripcion, peso, coste)
        self.__nombre = "Seat"
        self.componentes = componentes
        
    def __str__(self):
        return f"El coche {self.__nombre} esta compuesto por {self.componentes} {self.descripcion} con un peso por pieza de {self.peso} y un coste de {self.coste}"
    
class Piezas(Coche):
    
    def __init__(self, componentes, descripcion, peso, coste):
        super().__init__(Coche(componentes, descripcion, peso, coste))
        
c1 = Coche()
c2 = Piezas(1, "Motor", 150, 500)

print(c1 == c2)

print(c2)

p = puertaCoche(True)