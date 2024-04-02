import array

# Tipo enteros (int) son 'b' y 'B'
arr1 = array.array('B', [1, 4, 2, 4, 11])
print(arr1)

arr2 = array.array('B', range(10))
print(arr2)

arr2.extend(range(3))
print(arr2)

print(arr2.typecode)

print(arr2.itemsize)

# Crear un array de números decimales
dec = array.array('d', [0.0, 1.0, 2.0, 3.0, 4.449, 5.0, 6.0, 7.0, 8.0, 9.0])
print(dec)

# Como añadir elementos a una array
arr2.append(111)
print(arr2)

# Ver la longitud de un array
print(len(arr2))
print(arr2.__len__())

# Buscar la posicion que usa un elemento en un array
print(arr2.index(111))

# Insertar un elemnto en una posicion en concreto
arr2.insert(3, 120)
print(arr2)

# Saca una posicion en concreto de la lista
arr2.pop(5)
print(arr2)

# Invierte el array
arr2.reverse()
print(arr2)

# Borrar un elemento en concreto
arr2.remove(5)
print(arr2)

# Sacar por pantalla una posicion
print(arr2[3])

# Sacar por pantalla la última posicion
print(arr2[-1])

# El contenido de un array pasarlo a un fichero
arr3 = array.array('u', ["a", "b", "c"])

with open("./salida.txt", "ab") as f:
    arr3.tofile(f)
    
    arr2.tofile(f)
