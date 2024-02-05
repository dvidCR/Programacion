cadena =  input("¿Dime algo?: ")
contador = 0
for si in cadena:
    if (si == "a" or si == "e" or si == "i" or si == "o" or si == "u"):
        contador +=1
print (contador)