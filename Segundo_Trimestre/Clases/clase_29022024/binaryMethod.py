l = [1, 4, 6, 3, 1, 6, 8, 3, 1]


def binaryMethod(lista, numero):
    lista.sort()
    distinct = True
    min = 0
    max = len(lista)
    
    while(distinct):
        div = min // max
        if (lista[div] == numero):
            distinct = False
        elif (lista[div] > numero):
            max = div - 1
        elif (lista[div] < numero):
            min = div + 1
    
    return f"El número {numero} está en la posicion {div}"

print(binaryMethod(l, 8))