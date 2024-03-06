usuarios = {  
      "iperurena": {  
          "nombre": "Iñaki",  
		  "apellido": "Perurena",  
		  "password": "123123"  
	  },  
	  "fmuguruza": {  
	        "nombre": "Fermín",  
		  "apellido": "Muguruza",  
		  "password": "654321"  
	  },  
	  "aolaizola": {  
	       "nombre": "Aimar",  
		  "apellido": "Olaizola",  
		  "password": "123456"  
	  }  
}

cont = 0
noExit = True

while(cont < 3 and noExit):
    nombre = input("Escribe tu nombre: ")
    apellido = input("Escribe tu apellido: ")
    passwd = input("Escribe tu contraseña: ")
        
    for i in usuarios.values():
        if (i["nombre"] in nombre and i["apellido"] in apellido and i["password"] in passwd):
            print(f"Hola {nombre} {apellido}, has iniciado sesión correctamente.")
            noExit = False
            break

    if (noExit):
        print("Nombre, apellido o usuario no existente.")            
        cont+=1