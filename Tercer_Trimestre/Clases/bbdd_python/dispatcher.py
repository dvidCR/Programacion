from conexionBD import conexion2bd as bd
from contactos import contacto
from agendas import Agenda

class dispatcher:
    def __init__(self):
        self.__db = bd("root","","dam")
        self.__conn = self.__db.get_connection()
        self.agenda = Agenda()
    
    
    def cargarAgenda(self):
        mycursor = self.__conn.cursor()
        mycursor.execute("SELECT * FROM usuarios")
        myresult = mycursor.fetchall()

        for x in myresult:
            c = contacto (x[1],x[3],x[2])
            self.agenda.addContacto(c)
            
    def getAgenda(self):
        return self.agenda  
            
if __name__ == "__main__":
    d = dispatcher()
    d.cargarAgenda()
    for i in d.getAgenda().getAgenda():
        print (i.getName())