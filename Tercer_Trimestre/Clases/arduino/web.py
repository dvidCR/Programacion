class Web:
    
    def __init__(self):
        self.html = open("./cv.html", "w+")

    def crearHTML(self, humedad, temperatura):
        self.html.write("<!DOCTYPE html>\n") #0
        self.html.write("<html lang='es'>\n") #1
        self.html.write("<head>\n") #2
        self.html.write("<meta charset='UTF-8'>\n") #3
        self.html.write("<title>Termometro</title>\n") #4
        self.html.write("</head>\n") #5
        self.html.write("<body>\n") #6
        self.html.write("<h2>Humedad</h2>\n") #7
        self.html.write(f"<p>{humedad}</p>\n") #8
        self.html.write("<br><br>\n") #9
        self.html.write("<h2>Temperatura</h2>\n") #10
        self.html.write(f"<p>{temperatura}</p>\n") #11
        self.html.write("</body>\n") #12
        self.html.write("</html>\n") #13
        
    def close(self):
        self.html.close()