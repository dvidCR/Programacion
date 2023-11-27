class Cuenta:
    
    def __init__(self, titular, cantidad):
        self.titutlar = titular
        self.cantidad = cantidad
        
    def get_titular(self):
        print(self.titutlar)
        return self.titutlar
    
    def set_titular(self, titular):
        self.titutlar = titular
        print(titular)
        
    def get_cantidad(self):
        print(self.cantidad)
        return self.cantidad
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
        print(cantidad)
    
    def ingresar(self, ingreso):
        return self.cantidad + ingreso
        
    
    def retirar(self, retira):
        return self.cantidad - retira
    
c = Cuenta("Paco", 678)

c.get_titular()
c.get_cantidad()
c.ingresar(50)
c.get_cantidad()
c.retirar(10)
c.get_cantidad()

c.set_titular("Esteban")
c.set_cantidad(500)
c.get_titular()
c.get_cantidad()