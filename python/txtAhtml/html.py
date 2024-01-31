def pasarContenido():
    for i in html.readlines():
        match (i):
            case "nombre en h2":
               html.writelines("nombre en h2", fichero.readlines[0])
            
            case  "fecha de nacimiento":
               html.writelines("fecha de nacimiento", fichero.readlines[2])
                
            case "numero":
               html.writelines("numero", fichero.readlines[1])
                
            case "calle":
               html.writelines("calle", fichero.readlines[3])

def crearHTML():
    html.write("<!DOCTYPE html>\n") #0
    html.write("<html lang='es'>\n") #1
    html.write("<head>\n") #2
    html.write("<meta charset='UTF-8'>\n") #3
    html.write("<title>Curriculum Vitae</title>\n") #4
    html.write("</head>\n") #5
    html.write("<body>\n") #6
    html.write("nombre en h2\n") #7
    html.write("<img src='./foto_persona.jpg' width='100' height='100' id='foto'>\n") #8
    html.write("<br><br>\n") #9
    html.write("fecha de nacimiento\n") #10
    html.write("<br><br>\n") #11
    html.write("<strong>CONTACTO</strong>\n") #12
    html.write("<br><br>\n") #13
    html.write("numero\n") #14
    html.write("<br><br>\n") #15
    html.write("<strong>Direccion</strong>\n") #16
    html.write("<br><br>\n") #17
    html.write("calle\n") #18
    html.write("</body>\n") #19
    html.write("</html>\n") #20
    

def main():
    global html
    global fichero

    
    fichero = open("./ejemplo.txt", "r+")
    
    html = open("./cv.html", "w+")
            
    
        
    
    if html.read() == "":
        crearHTML()

    pasarContenido()
        
if __name__ == "__main__":
    main()