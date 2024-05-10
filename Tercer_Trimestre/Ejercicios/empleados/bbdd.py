import MySQLdb

class BBDD:
    
    def __init__(self, usuario, password, bbdd):
        self.connect2DB(usuario, password, bbdd)
        self.cursor = self.mibbdd.cursor()
    
    def connect2DB(self, usuario, password, bbdd):
        try:
            self.mibbdd = MySQLdb.connect("127.0.0.1", usuario, password, bbdd)
        except MySQLdb.Error as e:
            print(e)
    
    def ver(self):
        sql = "select * from empleados"
        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            
            return registros
                    
        except MySQLdb.Error as e:
            print(e)
    
    def nuevos(self, nombre, apellidos, dni, puesto, telefono):
        if not self.comprobarRepetidos(nombre, apellidos, dni):
            sql = f"insert into empleados(nombre, apellidos, dni, puesto, telefono, alta, baja) values ('{nombre}', '{apellidos}', '{dni}', '{puesto}', {telefono}, 1, 0)"
            try:
                self.cursor.execute(sql)
                self.mibbdd.commit()
                return True, ""
            except MySQLdb.Error as e:
                return False, f"Error al instertar: {e}"
        else:
            return False, f"Nombre, Apellidos y DNI duplicados"
    
    def altas_bajas(self, estado, nombre, apellidos, dni):
        if self.comprobarRepetidos(nombre, apellidos, dni):
            if estado == "alta":
                sql = f"update empleados set alta = 1, baja = 0 where nombre = '{nombre}' and apellidos = '{apellidos}' and dni = '{dni}'"
            elif estado == "baja":
                sql = f"update empleados set alta = 0, baja = 1 where nombre = '{nombre}' and apellidos = '{apellidos}' and dni = '{dni}'"
            try:
                self.cursor.execute(sql)
                self.mibbdd.commit()
                return True, ""
            except MySQLdb.Error as e:
                return False, f"Error al actualizar el estado: {e}"
        else:
            return False, f"Nombre, apellidos o DNI mal introducidos"
    
    def updateBBDD(self, estado, nombre, apellidos, dni, cambio):
        if self.comprobarRepetidos(nombre, apellidos, dni):
            sql = f"update empleados set {estado} = '{cambio}' where nombre = '{nombre}' and apellidos = '{apellidos}' and dni = '{dni}'"  
            try:
                self.cursor.execute(sql)
                self.mibbdd.commit()
                return True, ""
            except MySQLdb.Error as e:
                return False, f"Error a la hora de actualizar el {estado}: {e}"
        else:
            return False, f"Nombre, apellidos o DNI mal introducidos"
    
    def comprobarRepetidos(self, nombre, apellidos, dni):
        sql = f"select nombre, apellidos, dni from empleados where nombre = '{nombre}' and apellidos = '{apellidos}' and dni = '{dni}'"  
        try:
            self.cursor.execute(sql)
            registros = self.cursor.fetchall()
            if registros:
                return True
            else:
                return False
        except:
            return True