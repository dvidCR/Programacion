from bbdd import db
from Request import Request
from web import Web

class Main(db, Request, Web):
    
    def __init__(self):
        self.requests = Request("http://192.168.4.1")
        self.connect2DB("root", "", "temperatura")
    
    def conectarTermometro(self):
        self.requests.request()
        self.requests.conectar()
        
    def sacarContenido(self):
        self.humedad, self.temperatura = self.requests.contenido()
        print(self.humedad, self.temperatura)
        
    def instertarBBDD(self):
        self.update(self.humedad, self.temperatura)
        
    def HTML(self):
        humedad, temperatura = self.ver()
        web = Web()
        web.crearHTML(humedad, temperatura)
        web.close()
        
m = Main()
m.conectarTermometro()
m.sacarContenido()
m.instertarBBDD()
m.ver()