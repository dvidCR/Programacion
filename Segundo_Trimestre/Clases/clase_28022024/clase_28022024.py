pila = []

pila.append(2)
pila.append(5)
pila.append(2)
pila.append(8)
pila.append(0)

'''print(pila)

aux = pila.pop()
print(aux)
print(pila)'''

def reemplazar(pila, nuevo, viejo):
    pila2 = []
    for i in range(0, len(pila)):
        aux = pila.pop()
        if (aux == viejo):
            pila2.append(nuevo)
        else:
            pila2.append(aux)
    
    pila2.reverse()
    return pila2
    
print(reemplazar(pila, 7, 2))

l = [3, 4, 2, 1, 7, 3, 1]

def buscar(lista, numero):
    for i in range(0, len(lista)):
        if lista[i] == numero:
            return f"Esta en la posición {i}"
        
print(buscar(l, 7))