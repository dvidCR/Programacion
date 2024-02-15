from abc import ABC, abstractmethod

class Persona:
    
    def __init__(self, nombre, apellidos, NIF):
        self.nombre = nombre
        self.apellidos = apellidos
        self.nif = NIF

class Cuenta(Persona):
    
    def __init__(self, numerocuenta, saldo, cliente):
        self.numerocuenta = numerocuenta
        self.saldo = saldo
        self.cliente = [cliente]
        return super().__init__(cliente[0], cliente[1], cliente[2])
        
    def ingresar(self, dinero):
        if (dinero > 0):
            añadir = self.saldo + dinero
            ingresar = input(f"¿Seguro que quieres ingresar {dinero} a tu cuenta?")
            if (ingresar == "y"):
                self.actualizarSaldo(añadir)
        else:
            raise("No puedes añadir saldo negativo")
        
    @abstractmethod
    def retirar(self, dinero):
        pass
    
    def actualizarSaldo(self, añadir):
        self.saldo = añadir
        
class cuentaCorriente(Cuenta):
    
    def __init__(self):
        self.interes = 1.5
    
    def __str__(self):
        return f"El titular de la cuenta {self.cliente[0]} {self.cliente[1]} con el NIF {self.cliente[2]} y el número de cuenta {self.numerocuenta} tiene un saldo de {self.saldo}€ con un interes fijo del {self.interes}"
    
class cuentaAhorro(Cuenta):
    
    def __init__(self, interes, saldoMinimo):
        super().__init__()
        self.interes = interes
        self.saldoMinimo = saldoMinimo
        
    def retirar(self, dinero):
        if (self.saldo > self.saldoMinimo):
            if (self.saldo - dinero > 0):
                quitar = self.saldo - dinero
                retirar = input(f"¿Seguro que quieres ingresar {dinero} a tu cuenta?")
                if (retirar == "y"):
                    self.actualizarSaldo(quitar)
            else:
                raise("La cuenta no puede quedarse sin dinero ni en numeros rojos")
        else:
            raise(f"Error al retirar el dinero: Tu cuenta no puede bajar de los {self.saldoMinimo}€")
            
    def __str__(self):
        return f"El titular de la cuenta {self.cliente[0]} {self.cliente[1]} con el NIF {self.cliente[2]} y el número de cuenta {self.numerocuenta} tiene un saldo de {self.saldo}€ con un interes variable del {self.interes} y la cuenta no puede bajar de los {self.saldoMinimo}€"
    
    def añadirInteres(self):
        self.saldo = self.saldo - self.interes / 100
        
c = Cuenta(1, 50.0, ("Jose", "Martinez", "0258N"))
cc = cuentaCorriente()
print(cc)