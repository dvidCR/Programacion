# Solamente esta permitido el método len.
def borrar(l, n):
    print(lista)
    listado = []
    for i in range(0, len(l)):
        if (l[i] != n):
            listado = listado + [l[i]]

    return listado
        
lista = [1, 2, 3, 4, 4, 5]

lista = borrar(lista, 4)

print(lista)