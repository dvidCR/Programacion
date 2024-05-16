import MySQLdb

class conexion2bd():
    def __init__(self, usuario, passwd, bbdd):
    
        self.mydb = MySQLdb.connect( 
            "localhost",
            usuario,
            passwd,
            bbdd)
    
    def get_connection (self):
        return self.mydb