class ContactList(list):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.append(self)

class Contact:
    all_contact = ContactList
    
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if contact.name == name:
                matching_contacts.append(contact.name)
        return matching_contacts
    
contacto1 = ContactList("Juan", "juan@gmail.com")

contacto2 = ContactList("Pedro", "pedro@gmail.com")

contacto3 = ContactList("Mario", "mario@gmail.com")

nombre = input("Que nombre quiere buscar: ")

print (Contact.all_contact.search("Mario"))
    


#Agrega un método llamado search a la clase ContactList que tome un argumento name.
#Dentro del método search, inicializa una lista vacía llamada matching_contacts.
#Itera sobre la lista self y verifica si el name proporcionado está contenido en el nombre del contacto. Si es así, agrega el contacto a matching_contacts.
#Retorna matching_contacts al final del método.