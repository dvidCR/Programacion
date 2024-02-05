class cuentaBancaria:
    
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self,añadir):
        self.saldo = self.saldo + añadir
        
    def retirar(self,quitar):
        if (self.saldo > 0):
            self.saldo = self.saldo - quitar
        else:
            print("Dinero insuficiente")
            
    def visualizar(self):
        print("Bienvenido " + str(self.titular))
        print("")
        print("Dinero total en la cuenta: " + str(self.saldo) + "€")
        print("")