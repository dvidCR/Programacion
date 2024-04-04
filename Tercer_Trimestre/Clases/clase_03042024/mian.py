import array

# #crea un array de una lista de elementos del 1 al 100

lista = array.array("b", range(1, 101))  
print(lista)  

#añade el 12345 al final a la vez

lista.extend(range(1, 6))
print(lista)

#calcula el tamaño de la lista

print(lista.__len__())
print(len(lista))

#sustituye el elemento de la posicion 2

lista.pop(2)
lista.insert(2, 59)
lista[6] = 77
print(lista)

#sacalo a un fichero fichero.txt

with open("fichero.txt", "wb") as f:
    lista.tofile(f)
    print(lista)

# Lee el contenido del archivo y lo imprime
with open("fichero.txt", "rb") as f:
    print(f.read())