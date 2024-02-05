from cuentaBancaria import *
import sys
import os

nombre = input("Nombre de la cuenta, porfavor: ")
cuenta = cuentaBancaria(nombre, 1000)

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
            os.system("cls")
            print("//////////////////CAJERO AUTOMATICO////////////////////")
            print("\n")
            añadir = int(input("¿Cuanto dinero quieres añadir?: "))
            cuenta.depositar(añadir)
            os.system("cls")
        case 2:
            os.system("cls")
            print("//////////////////CAJERO AUTOMATICO////////////////////")
            print("\n")
            quitar = int(input("¿Cuanto dinero quires retiar?: "))
            cuenta.retirar(quitar)
            os.system("cls")
        case 3:
            os.system("cls")
            print("//////////////////CAJERO AUTOMATICO////////////////////")
            print("\n")
            cuenta.visualizar()
            os.system("Pause")
            os.system("cls")
        case 4:
            os.system("cls")
            sys.exit()