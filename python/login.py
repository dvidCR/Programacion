class LoginError(Exception):
    
    pass

class Login:
    
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password
        
    def validacion(self, usuario, password):
        if(self.usuario == usuario and self.password == password):
            print("Todo bene")
        else:
            raise LoginError("Usuario o contraseña invalido")

try:     
    Login("pepe", "123").validacion("pepa", "123")
except LoginError as e:
    print("Usuario o contraseña invalido")