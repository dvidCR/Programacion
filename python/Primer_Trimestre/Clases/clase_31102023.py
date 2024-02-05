class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
    
    def imprimirContactoactual(self):
        print(f'{self.name + " --> " + self.email}')
        
class Supplier(Contact):
    def order(self, order):
        print("Si este fuera un sistema real, enviaríamos el pedido '{}' a '{}'".format(order, self.name))

c = Contact("Jose", "jose@gmail.net")

name = input("Escribe tu nombre: ")
email = input("Escribe tu email: ")

supp = Supplier(name, email)

supp.order("Esta es la orden 1")

supp.imprimirContactoactual()

for i in Contact.all_contacts:
    print(i.name, i.email)