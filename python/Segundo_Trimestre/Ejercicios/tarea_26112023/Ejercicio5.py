from abc import ABC, abstractmethod
import os

class Archivo(ABC):
    
    @abstractmethod
    def abrir(self):
        pass
    
    @abstractmethod
    def cerrar(self):
        pass
    
    @abstractmethod
    def leer(self):
        pass

class ArchivoTexto(Archivo):
    
    def __init__ (self, contenido):
        self.contenido = contenido
        
    def abrir(self):
        print(f"\nAbres el archivo {self.contenido}")
        
    def cerrar(self):
        print(f"\nCierras el archivo {self.contenido}")
        
    def leer(self):
        print(f"\n{self.contenido}")
        
class ArchivoImagen(Archivo):
    
    def __init__ (self, contenido):
        self.contenido = contenido
        
    def abrir(self):
        print(f"\nAbres el archivo {self.contenido}")
        
    def cerrar(self):
        print(f"\nCierras el archivo {self.contenido}")
        
    def leer(self):
        print(f"\nIntentas leer el contenido del archivo {self.contenido}, pero recuerdas que es una imagen y abres un lector de imagenes")
        
class ArchivoAudio(Archivo):
    
    def __init__ (self, contenido):
        self.contenido = contenido
        
    def abrir(self):
        print(f"\nAbres el archivo {self.contenido}")
        
    def cerrar(self):
        print(f"\nCierras el archivo {self.contenido}")
        
    def leer(self):
        print(f"\nIntentas leer el contenido del archivo {self.contenido}, pero se te ha olvidado activar los subtitulos")
        
cerrar = True

while(cerrar == True):
    a = input("Pon el nombre del archivo que quieras abrir: ")
    
    t = int(input("Que tipo de archivo es(1 , 2, 3) \n1. De texto \n2. De Imagen \n3. De sonido \n:"))
    
    try:
        match t:
            case 1:
                ArchivoTexto(a).abrir()
            
            case 2:
                ArchivoImagen(a).abrir()
                
            case 3:
                ArchivoAudio(a).abrir()
    
    except NameError as e:
        print(e)
        
    l = input("Quieres leer el archivo (s, n): ")
    
    try:
        match l:
            case "s":
                if t == 1:
                    ArchivoTexto(a).leer()
                    os.system("pause")
                elif t == 2:
                    ArchivoImagen(a).leer()
                    os.system("pause")
                elif t == 3:
                    ArchivoAudio(a).leer()
                    os.system("pause")
            case "n":
                pass
            
    except NameError as e:
        print(e)
        
    c = input("Quieres cerrar el archivo (s, n): ")
    try:
        match c:
            case "s":
                if t == 1:
                    ArchivoTexto(a).cerrar()
                    os.system("pause")
                    cerrar = False
                elif t == 2:
                    ArchivoImagen(a).cerrar()
                    os.system("pause")
                    cerrar = False
                elif t == 3:
                    ArchivoAudio(a).cerrar()
                    os.system("pause")
                    cerrar = False
            case "n":
                pass
    
    except NameError as e:
        print(e)