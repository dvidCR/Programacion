l = [1, 4, 6, 3, 1, 6, 8, 3, 1]

def burbuja(lista):
    new = []
    for i in range(0, len(lista)):
        aux = lista[i]
        pos = i
        for j in range(1, len(lista) - 1):
            if (lista[j] > aux):
                aux = lista[j]
                pos = j
        
        r = lista.pop(pos)     
        new.append(r)
        lista.append(0)
        
    return new

print(burbuja(l))