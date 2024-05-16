import MySQLdb
import sys

class BBDD:
    
    def __init__(self):
        pass

    def connect(self, bbdd):
        self.mibbdd = MySQLdb.connect("127.0.0.1", "root", "", bbdd)
        self.cursor = self.mibbdd.cursor()
        
    def insert(self, año, mes, solicitud, intervencion, codigo, distrito, hospital):
        sql = f"insert into activaciones(Año, Mes, horaSolicitud, horaIntervencion, Codigo, Distrito, Hospital) values ('{año}', '{mes}', '{solicitud}', '{intervencion}', '{codigo}', '{distrito}', '{hospital}')"
        try:
            self.cursor.execute(sql)
            self.mibbdd.commit()
        except MySQLdb.Error as e:
            print(f"Error al instertar: {e}")
            sys.exit()
        
    