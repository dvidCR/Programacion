# --> Ejercicio 1

#pregunta = int(input("Pon un número: "))
#suma = 0
#while (suma < 100):
#    pregunta2 = int(input("¿Por cuanto quieres sumar el " + str(pregunta) + " ?: "))
#    suma = pregunta + pregunta2
#    pregunta = suma
#    print(pregunta)

# --> Ejercicio 2

import sys
import os

dinero = 1000

def visualizar():
    estado = str(dinero) + "€"
    print (estado)

while (True):
    print("//////////////////CAJERO AUTOMATICO////////////////////")
    print("\n")
    print("1. Depositar dinero a la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Ver el estado de la cuenta")
    print("4. Retirar la tarjeta")
    print("\n")
    print("///////////////////////////////////////////////////////")
    menu = int(input("Escoga una opcion: "))

    match menu:
        case 1:
            depositar = int(input("¿Cuanto dinero quieres añadir?: "))
            dinero = dinero + depositar
            os.system("cls")
        case 2:
            retirar = int(input("¿Cuanto dinero quieres retiar?: "))
            dinero = dinero - retirar
            os.system("cls")
        case 3:
            visualizar()
            os.system("Pause")
            os.system("cls")
        case 4:
            os.system("cls")
            sys.exit()