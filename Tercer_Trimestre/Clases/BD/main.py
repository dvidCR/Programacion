import MySQLdb
import sys

class db:
    
    def __init__(self):
        pass
    
    def connect2DB(self, usuario, password, bbdd):
        try:
            self.mibbdd = MySQLdb.connect("127.0.0.1", usuario, password, bbdd)
            print(f"Te has conectado correctamente a la base de datos {bbdd}")
        except MySQLdb.Error as e:
            print(e)
            sys.exit()
            
    def insert(self, nombre, edad, apellidos):
        cursor = self.mibbdd.cursor()
        if self.comprobarRepetidos(nombre, apellidos):
            sql = f"insert into usuarios(nombre, edad, apellidos) values ('{nombre}', {edad}, '{apellidos}')"
            print("Ejecutando el insert")
            print(sql)
            try:
                cursor.execute(sql)
                self.mibbdd.commit()
            except MySQLdb.Error as e:
                print(f"Error al instertar {e}")
            
    def consultarUsuario(self):
        cursor = self.mibbdd.cursor()
        sql = "select * from usuarios"
        try:
            cursor.execute(sql)
            print(f"Numero de filas... {cursor.rowcount}")
            registros = cursor.fetchall()
            
            for i in registros:
                print(str(i[0]) + " | "+ str(i[1]) + " | " +str(i[2]) + " | " + str(i[3]))
                    
        except MySQLdb.Error as e:
            print(e)
            
    def consultaPersonalizada(self, tipo, consulta):
        cursor = self.mibbdd.cursor()
        if consulta == int:
            sql = f"select * from usuarios where {tipo} = {consulta}"
        else:
            sql = f"select * from usuarios where {tipo} = '{consulta}'"
            
        try:
            cursor.execute(sql)
            registros = cursor.fetchall()
            print(registros)
                    
        except MySQLdb.Error as e:
            print(e)
            
            
    def comprobarRepetidos(self, nombre, apellidos):
        cursor = self.mibbdd.cursor()
        sql = f"select nombre, apellidos from usuarios where nombre = '{nombre}' and apellidos = '{apellidos}'"  
        try:
            cursor.execute(sql, (nombre, apellidos))
            return True
        except MySQLdb.Error as e:
            print(f"Nombre y apellidos duplicados: {e}")
            return False
        
if __name__ == "__main__":
    mi_base_datos = db()
    mi_base_datos.connect2DB("root", "", "DAM")
    mi_base_datos.insert("Alfonso", 44, "Folagor")
    mi_base_datos.consultarUsuario()
    mi_base_datos.consultaPersonalizada("edad", 44)