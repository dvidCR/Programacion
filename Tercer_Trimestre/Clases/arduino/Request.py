import requests
from bs4 import BeautifulSoup


class Request:
    
    def __init__(self, url):
        self.url = url

    def request(self):
        self.response = requests.get(self.url)
        
    def verificar(self):
        if self.response.status_code == 200:
            return True
        return False

    def conectar(self):
        if(self.verificar()):
            self.html_content = self.response.text
            self.soup = BeautifulSoup(self.html_content, 'html.parser')
        else:
            print("Error al acceder a la página:", self.response.status_code)

    def contenido(self):
        frase = self.soup.prettify().replace(":", " ")
        frase = frase.split(" ")
        
        return frase[2], frase[5]