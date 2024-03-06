# obtener el numero mayor de la lista
l = [1, 4, 6, 3, 1, 6, 8, 3, 1]
aux = 0

for i in range(0, len(l)):
    if (l[i] < aux) or (aux == 0):
        aux = l[i]
        
print(aux)

def buscar(lista, numero):
    for i in range(0, len(lista)):
        if lista[i] == numero:
            return f"Esta en la posición {i}"
        
print(buscar(l, 6))