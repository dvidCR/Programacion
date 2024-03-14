'''En	un	archivo	de	 texto	inventario.txt se guarda información acerca	de los	
productos existentes en	 un	 almacén. Para cada	 producto	 se	 guardan	 los	
siguientes	datos:	
 Código	del	producto	(entero	positivo)	
 Nombre	del	producto	
 Número	de	unidades	(entero)	
 Precio	por	unidad	(real)	
El	archivo	está	ordenado	por	orden	creciente	del	código	de	producto	y	termina	
con	un	‐1	como	código.	'''

import os

if (os.getcwd != "D:/Clase/Programacion/Segundo_Trimestre/Clases/repaso_examen2"):
    os.chdir("D:/Clase/Programacion/Segundo_Trimestre/Clases/repaso_examen2")

productos = {}

class Inventario:
    def __init__(self, codigo, nombre, unidades, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.unidades = unidades
        self.precio = precio
        
        self.inventario = open("./inventario.txt", "w+")
        
    def añadirCola(self):
        productos.update({"Producto" + str(len(productos)): {"Codigo": self.codigo, "Nombre": self.nombre, "Unidades": self.unidades, "Precio": self.precio}})
        
    def añadirInventario(self):
        os.system("cls")
        print(productos)
        comp = input("¿Estas seguro de querer añadir estos datos al inventario? (y/n): ")
        if (comp == "y"):
            for i in range(0, len(productos)):
                self.inventario.write(productos[f"Producto{i}"]["Codigo"])
                self.inventario.write(productos[f"Producto{i}"]["Nombre"])
                self.inventario.write(str(productos[f"Producto{i}"]["Unidades"]))
                self.inventario.write(str(productos[f"Producto{i}"]["Precio"]))
        
    def leerProductos(self):
        os.system("cls")
        print(productos)
        os.system("Pause")
        
    def leerInventario(self):
        os.system("cls")
        self.inventario.read()
        os.system("Pause")
        
    def comprobar(self):
        for i in range(0, len(self.inventario.readline())):
            pass
        
    def salir(self):
        self.inventario.close()

i = Inventario(None, None, None, None)

continuar = True

while(continuar):
    os.system("cls")
    op = int(input(("--------------------------------------------------------------------------------\n \
        ¿Que quieres hacer?\n \
        1. Añadir productos a la cola para luego insertarlos todos\n \
        2. Añadir productos de la cola al inventario\n \
        3. Leer los productos que tienes en cola\n \
        4. Leer los productos que ya están en el inventario\n \
        5. Salir\n \
        : ")))

    match (op):
        case 1:
            print("----------------------------------------------------------")
            codigo = input("Añade el código del producto: ")
            nombre = input("Añade el nombre del producto: ")
            unidades = int(input("Añade el número de unidades: "))
            precio = float(input("Añade el precio del producto por unidad: "))
            '''if (i.comprobar()):
                i.__init__(codigo, nombre, unidades, precio)
                i.añadirCola()
            else:
                print("Código de producto ya existente")'''
            i.__init__(codigo, nombre, unidades, precio)
            i.añadirCola()

        case 2:
            i.añadirInventario()
        
        case 3:
            i.leerProductos()
            
        case 4:
            i.leerInventario()
            
        case 5:
            i.salir()
            continuar = False