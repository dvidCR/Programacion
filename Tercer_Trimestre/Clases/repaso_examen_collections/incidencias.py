'''
Crear un programa de gestión de incidencias donde cada incidencia hay que guardar:
    clave, descripción, usuario que pone la incidencia y nombre técnico.
Tiene que tener un contador del tipo de incidencia para ir contabilizando las incidencias por

Tienes que utilizar al menos 3 clases de collections.
'''

from collections import Counter, defaultdict, deque

class Incidencias:
    
    def __init__(self, clave, descripcion, usuario, nombre_tecnico):
        self.clave = clave
        self.descripcion = descripcion
        self.usuario = usuario
        self.nombre_tecnico = nombre_tecnico
        self.nuevasIncidencias = deque([self.clave, self.descripcion, self.usuario, self.nombre_tecnico])
        self.iniciarIncidencia()

    def iniciarIncidencia(self):
        self.fichero = open("./incidencias.txt", "a+")
        self.incidencias = deque(self.fichero.read())
        
    def añadirIncidencia(self):
        self.nuevasIncidencias = str(self.nuevasIncidencias).replace("deque(", "")
        self.nuevasIncidencias = str(self.nuevasIncidencias).replace(")", ",")
        self.fichero.write(str(self.nuevasIncidencias))
        
    def comprobarClave(self, clave):
        for i in range(len(self.incidencias)):
            if(clave == self.incidencias[i][0] or self.clave == None):
                return False
            
        return True
    
    def contabilizar(self):
        return Counter(self.incidencias)
        
    @property
    def verIncidencias(self):
        return self.incidencias
    
    @verIncidencias.setter
    def actualizarIncidencias(self, clave, cambio, pos):
        for i in range(len(self.incidencias)):
            if self.incidencias[i][0] == clave:
                self.incidencias.pop(pos)
                self.incidencias.insert(pos, cambio)
                break
            
    def close(self):
        self.fichero.close()
        
if __name__ == "__main__":
    i = Incidencias(None, None, None, None)
    seguir = True
    
    while(seguir):
        op = int(input("-----------------------------------------------------------------------------------\n\
                                            Menu de incidencias\n\
            1. Añadir incidencia\n\
            2. Actualizar una incidencia\n\
            3. Ver incidencias\n\
            4. Contabilizar Incidencias\n\
            5. Salir\n\
            : "))
        
        match(op):
            case 1:
                clave = input("Añade la clave de la incidencia (¡¡No se pueden repetir las claver de las incidencias!!): ")
                descripcion = input("Añadele una descripcion a la incidencia: ")
                usuario = input("Pon el nombre del usuario que ha abierto tiquet: ")
                nombre_tecnico = input("Pon el nombre tecnico de esta incidencia: ")
                if(i.comprobarClave(clave)):
                    i = Incidencias(clave, descripcion, usuario, nombre_tecnico).añadirIncidencia()
            case 2:
                clave = input("Tienes que poner la clave de la incidencia a la que le quieras cambiar algo: ")
                pos = int(input("¿Que quieres cambiar?\n\
                    1. Clave\n\
                    2. Descripcion\n\
                    3. Nombre del usuario que creo el ticket\n\
                    4. Nombre tecnico de la incidencia\n\
                    : "))
                cambio = input("¿Por que lo vas a cambiar?: ")
                
                if(pos == 1 and i.comprobarClave(cambio)):
                    i.actualizarIncidencias(clave, cambio, pos)
                    
            case 3:
                print(i.verIncidencias())
            
            case 4:
                print(i.contabilizar())
                
            case 5:
                i.close()
                seguir = False