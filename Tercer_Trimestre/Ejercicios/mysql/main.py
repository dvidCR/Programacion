import MySQLdb

class UI:
    
    def __init__(self):
        pass
    
    def conexion(self, usuario, contraseña):
        try:
            self.mibbdd = MySQLdb.connect("127.0.0.1", usuario, contraseña)
            self.cursor = self.mibbdd.cursor()
            print(f"Conectando a la base de datos")
        except MySQLdb.Error as e:
            print(e)
            
    def changeDB(self, bbdd):
        sql = f"use {bbdd}"
        try:
            self.cursor.execute(sql)
        except MySQLdb.Error as e:
            print(e)
            
    def crearBD(self, nombre):
        sql = f"create database {nombre}"
        try:
            self.cursor.execute(sql)
            print(f"CREANDO LA BASE DE DATOS {nombre}")
            self.mibbdd.commit()
        except MySQLdb.Error as e:
            print(e)
            
    def createTable(self, nombre):
        sql = f"create table {nombre} (id int primary key, nombre varchar(100), categoria varchar(50), cantidad int, precio double);"
        try:
            self.cursor.execute(sql)
            print(f"CREANDO LA TABLA {nombre}")
            self.mibbdd.commit()
        except MySQLdb.Error as e:
            print(e)
            
    def insert(self, nombre , categoria, cantidad, precio):
        sql = f'''insert into productos
                (nombre, categoria, cantidad, precio) 
                values 
                ('{nombre}', '{categoria}', {cantidad}, {precio})'''
        try:
            self.cursor.execute(sql)
            print(f"Insertando valores")
            self.mibbdd.commit()
        except MySQLdb.Error as e:
            print(e)
            
    def update(self, columna, cambio):
        if columna != "id":
            sql = f"update productos set {columna} = {cambio}"
            try:
                self.cursor.execute(sql)
                print(f"Insertando valores")
                self.mibbdd.commit()
            except MySQLdb.Error as e:
                print(e)
        else:
            print("No puedes cambiar el id")
            
    def ver(self):
        sql = "select * from productos"
        try:
            self.cursor.execute(sql)
            print(self.cursor.fetchall())
        except MySQLdb.Error as e:
            print(e)
    
    def salir(self):
        self.mibbdd.close()
            
if __name__ == "__main__":
    u = UI()
    u.conexion("root", "")
    # u.crearBD("TechStore")
    u.changeDB("TechStore")
    # u.createTable("productos")
    # u.insert("Ordenador", "Electronica", 1, 799.99)
    u.update("precio", 999.99)
    u.ver()
    u.salir()