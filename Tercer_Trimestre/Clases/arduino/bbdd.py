import MySQLdb
import sys

class db:
    
    def __init__(self):
        pass
    
    def connect2DB(self, usuario, password, bbdd):
        try:
            self.mibbdd = MySQLdb.connect("127.0.0.1", usuario, password, bbdd)
            self.cursor = self.mibbdd.cursor()
            print(f"Te has conectado correctamente a la base de datos {bbdd}")
        except MySQLdb.Error as e:
            print(e)
            sys.exit()
            
    def update(self, humedad, temperatura):
        if humedad != "nan" or temperatura != "nan":
            sql = f"update temperatura set Humedad = {humedad}, Temperatura = {temperatura}"
            try:
                self.cursor.execute(sql)
                self.mibbdd.commit()
            except MySQLdb.Error as e:
                print(f"Error al actualizar: {e}")
        else:
            print("No puede añadir la temperatura o la humedad vacia")
            
    def ver(self):
        sql = "select * from temperatura"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            print(datos[0])
            return datos[0]
        except MySQLdb.Error as e:
            print(e)
        