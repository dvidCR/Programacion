class Agenda ():
    
    def __init__(self):
        self.agenda= []
        
    def addContacto (self,contacto):
        self.agenda.append(contacto)
        
    def getAgenda (self):
        return self.agenda