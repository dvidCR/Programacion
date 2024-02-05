import socket
import os
from aplication import Aplication

class Cliente(Aplication):

    def __init__(self, puerto = 3000):
        
        self.host = socket.gethostname()
        self.port = puerto
        self.socket_client = socket.socket()
    
    def mensajes(self):
        
        self.mensaje = input("-> ")
        
        self.socket_client.send(self.mensaje.encode())
        
    def recibir(self):
        self.datos = self.socket_client.recv(1024).decode()
        
        print("Mensaje del servidor " + self.datos)
        
        os.system("Pause")
    
    def conectar(self):
        
        self.socket_client.connect((self.host,self.port))
        
        while(True):
            
            op = int(input("1. Enviar mensaje al servidor\n2. Recibir mensajes\n3. Abrir una aplicación\n4. Cerrar aplicación\n5. Salir\n-> "))
            
            match op:
                case 1:
                    self.mensajes()
                    
                case 2:
                    self.recibir()
                    
                case 3:
                    open("./aplication.py")
                    app = input("-> Que aplicacion quieres abrir\n-> ")
                    self.abrir(app.lower())
                    
                case 4:
                    open("./aplication.py")
                    app = input("-> Que aplicacion quieres cerrar\n-> ")
                    self.cerrar(app.lower())
                    
                case 5:
                    break
            
        self.socket_client.close()
    
if __name__ == '__main__':
    Cliente().conectar()