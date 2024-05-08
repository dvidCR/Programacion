import MySQLdb

class BBDD:
    
    def __init__(self, usuario, password, bbdd):
        self.mibbdd = MySQLdb.connect("127.0.0.1", usuario, password, bbdd)
    
    def altas(self, nombre, apellidos, dni, puesto, telefono):
        pass