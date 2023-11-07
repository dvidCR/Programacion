class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        
class Supplier(Contact):
    def order(self, order):
        print("Si este fuera un sistema real, enviaríamos el pedido '{}' a '{}'".format(order, self.name))

name = input("Escribe tu nombre: ")
email = input("Escribe tu email: ")
cont = Contact(name,email)
supp  = Supplier.order(cont,"Cascos")