cuadricua = ["_","_","_","_","_","_","_","_","_"]


def anadirValor(poscion, valor):
    cuadricua[poscion-1] = valor

def comprobarPosicion(poscion):
    if (cuadricua[poscion-1] == "_"):
        return True
    else:
        return False

def visualizar ():

    print("\n")
    print (cuadricua[0] + "|" + cuadricua[1] + "|" + cuadricua[2])
    print (cuadricua[3] + "|" + cuadricua[4] + "|" + cuadricua[5])
    print (cuadricua[6] + "|" + cuadricua[7] + "|" + cuadricua[8])
    print("\n")

nada = 3
while(nada == 3):
    while(True):
            poscion1 = input("Jugador 1: ¿Que posicion quieres?: ")
            if (poscion1 != 0) or (poscion1 < 10):
                comprobacion1 = comprobarPosicion(int(poscion1)) 
                if (comprobacion1 == True):
                    anadirValor(int(poscion1),"x")
                    visualizar()
    if (cuadricua[0] and cuadricua[1] and cuadricua[2] == "x") or (cuadricua[3] and cuadricua[4] and cuadricua[5] == "x") or (cuadricua[6] and cuadricua[7] and cuadricua[8] == "x") or (cuadricua[0] and cuadricua[3] and cuadricua[6] == "x") or (cuadricua[1] and cuadricua[4] and cuadricua[7] == "x") or (cuadricua[2] and cuadricua[5] and cuadricua[8] == "x") or (cuadricua[0] and cuadricua[4] and cuadricua[8] == "x") or (cuadricua[2] and cuadricua[4] and cuadricua[6] == "x"):
        print ("Jugador 1 gana")
        break
    while(True):
            poscion2 = input("Jugador 2: ¿Que posicion quieres?: ")
            if (poscion2 != 0) or (poscion2 < 10):
                comprobacion2 = comprobarPosicion(int(poscion2))
                if (comprobacion2 == True):
                    anadirValor(int(poscion2),"o")
                    visualizar()
    if (cuadricua[0] and cuadricua[1] and cuadricua[2] == "o") or (cuadricua[3] and cuadricua[4] and cuadricua[5] == "o") or (cuadricua[6] and cuadricua[7] and cuadricua[8] == "o") or (cuadricua[0] and cuadricua[3] and cuadricua[6] == "o") or (cuadricua[1] and cuadricua[4] and cuadricua[7] == "o") or (cuadricua[2] and cuadricua[5] and cuadricua[8] == "o") or (cuadricua[0] and cuadricua[4] and cuadricua[8] == "o") or (cuadricua[2] and cuadricua[4] and cuadricua[6] == "o"):
        print ("Jugador 2 gana")
        break