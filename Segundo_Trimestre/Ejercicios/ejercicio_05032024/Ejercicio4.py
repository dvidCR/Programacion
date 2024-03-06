estudiantes = {  
   "1": {  
	  "nombre": "Lorea",  
	  "nota": 8  
  },  
  "2": {  
      "nombre": "Markel",  
	  "nota": 4.2 
  },  
  "3": {  
      "nombre": "Julen",  
	  "nota": 6.5  
  }  
}

while(len(estudiantes) < 10):
    nombre = input("Pon el nombre del estudiante: ")
    nota = float(input("Pon su nota final: "))
    
    estudiantes.update({len(estudiantes)+1: {"nombre": nombre, "nota": nota}})
    
print(estudiantes)

for i in estudiantes.values():
    if (i["nota"] < 5):
        print(str(i["nombre"]) + " ha suspendido con un " +  str(i["nota"]))