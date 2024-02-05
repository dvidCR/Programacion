numero1 = int(input("Escoge un numero: "))
numero2 = int(input("Escoge un numero: "))
numero3 = int(input("Escoge un numero: "))
numero4 = int(input("Escoge un numero: "))

if (numero1 > numero2) and (numero1 > numero3) and (numero1 > numero4):
    print(numero1)
if (numero2 > numero1) and (numero2 > numero3) and (numero2 > numero4):
    print(numero2)
if (numero3 > numero1) and (numero3 > numero2) and (numero3 > numero4):
    print(numero3)
if (numero4 > numero1) and (numero4 > numero2) and (numero4 > numero3):
    print(numero4)