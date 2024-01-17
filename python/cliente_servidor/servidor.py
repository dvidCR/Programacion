import socket
import os
from aplication import Aplication

class Servidor(Aplication):

    def __init__(self, puerto = 3000):
        
        self.host = socket.gethostname()
        self.port = puerto
        
        #Creamos el socket para comunicarlo
        self.server_socket = socket.socket()
        
    def enviar(self):
        
        self.data = input("Escribe al cliente -> ")
            
        self.conn.send(self.data.encode())
        
    def recibir(self):
        
        self.datos = self.conn.recv(1024).decode()
            
        #if not self.datos:
        #    break
            
        print("Enviado desde el cliente " + self.datos)
        
        os.system("Pause")
    
    def servidor(self):
        
        #Asociamos al socket la dirección y el puerto
        self.server_socket.bind((self.host,self.port))
        
        #Número de clientes que puede atender mi sevidor depende del número
        self.server_socket.listen(2)
        
        self.conn,self.address = self.server_socket.accept()
    
        while(True):
            
            op = int(input("1. Enviar mensaje al cliente\n2. Recibir mensajes\n3. Abrir una aplicación del cliente\n4. Cerrar aplicación cliente\n5. Mover el raton del cliente de manera aleaoria\n6. Salir\n-> "))
            
            match op:
                case 1:
                    self.enviar()
                    
                case 2:
                    self.recibir()
                    
                case 3:
                    open("./aplication.py")
                    app = input("-> Que aplicacion quieres abrir\n-> ")
                    self.abrir(app.lower(), 999)
                    
                case 4:
                    open("./aplication.py")
                    app = input("-> Que aplicacion quieres cerrar\n-> ")
                    self.cerrar(app.lower(), 999)
                
                case 5:
                    open("./aplication.py")
                    self.moverMouse()
                    
                case 6:
                    break
            
        self.conn.close()
    
if __name__ == '__main__':
    server = Servidor().servidor()