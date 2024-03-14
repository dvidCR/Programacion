import os
from abc import ABC, abstractmethod

if (os.getcwd() != "D:/Clase/Programacion/Examenes/Examen2ºTrimestreP2"):
    os.chdir("D:/Clase/Programacion/Examenes/Examen2ºTrimestreP2")

class Buckup(ABC):
    
    def __init__(self):
        self.copia = open("./buckup.txt", "w+")
        self.update = open("./buckup.txt", "a+")
    
    @abstractmethod
    def buckup(self):
        pass
    
    @abstractmethod
    def actualizar(self):
        pass

class Mecanico(Buckup):
    
    def __init__(self, nombre, unidades, precio):
        self.nombre = nombre
        self.unidades = unidades
        self.precio = precio
        
        self.inventario = open("./inventario.txt", "r")
        
    def leerInventario(self):
        with open("./inventario.txt", "r") as i:
            print(i.read())
            
    def piezasTotales(self):
        aux = 0
        aux2 = 2
        for i in range(len(self.inventario.readlines())):
            try:
                with open("./inventario.txt", "r") as p:
                    aux3 = int(p.readlines()[aux2])
                    aux = aux + aux3
                    aux2+=4
            except:
                break
        
        return aux
    
    def comprobarContenido(self, unidades):
        aux = m.piezasTotales() + unidades
        if(aux < 500):
            return True
        else:
            return False
           
    def añadirPiezas(self):
        with open("./inventario.txt", "a+") as a:
            a.write(f"\n{self.nombre}\n{self.unidades}\n{self.precio}\n")
    
    #Ejercicio 2     
    def buckup(self):
        super().__init__()
        with open("./inventario.txt", "r") as b:
            self.copia.write(b.read())
            self.copia.close()
            
    #Ejercicio 3
    def actualizar(self):
        super().__init__()
        for i in range(0, len(self.inventario.readlines())):
            try:
                with open("./inventario.txt", "r") as actu:
                    if(actu.readlines()[i] != self.update.readlines()[i]):
                        self.update.write(actu.readlines()[i])
            except:
                pass
                        
        self.update.close()
            
    def salir(self):
        self.inventario.close()
    

         
m = Mecanico(None, None, None)

continuar = True

while(continuar):
    os.system("cls")
    op = int(input(("--------------------------------------------------------------------------------\n \
        ¿Que quieres hacer?\n \
        1. Leer inventario\n \
        2. Piezas totales en el inventario\n \
        3. Añadir piezas al inventario\n \
        4. Hacer copia de seguridad nueva\n \
        5. Actualizar copia de seguridad\n \
        6. Salir\n \
        : ")))

    match(op):
        case 1:
            os.system("cls")
            m.leerInventario()
            os.system("Pause")
            
        case 2:
            os.system("cls")
            print(m.piezasTotales())
            os.system("Pause")
            
        case 3:
            os.system("cls")
            print("----------------------------------------------------------")
            nombre = input("Añade el nombre de la pieza: ")
            unidades = int(input("Añade el número de piezas: "))
            precio = float(input("Añade el precio de l pieza por unidad: "))
            
            if(m.comprobarContenido(unidades)):
                m.__init__(nombre, unidades, precio)
                m.añadirPiezas()
            else:
                print("No puedes comprar más piezas")
                os.system("Pause")
        
        case 4:
            m.buckup()
        
        case 5:
            m.actualizar()
        
        case 6:
            os.system("cls")
            m.salir()
            continuar = False