a = [1,2,3,4,5,4]
a1 = [2, 16, 33]
b = ["a", "b", "c", "d"]
c = "holaquetal"

print(a[0])
print(b[0])
print(c[0])

# Añade un elemento a la lista.
a.append(6)

# Muestra el número de elementos de una lista.
print(len(a))

# Extend une el contenido de una lista a la otra.
# Los elemento repetidos no los pone.
a.extend(a1)
print(a)
print("-----------------------")

# Coge el último elemento y lo borra de la lista.
print(a.pop())

# Ordena la lista.
a.sort()
print(a)

# Da la posicion de un elemento.
print(a.index(5))

# Borra el elemento de la lista que le pases !!Si lo encuentra.
a.remove(6)
print(a)

# Insertar el 55 en la posicion 3 de la lista a.
a.insert(2, 55)
print(a)

# Le da la vuelta a la lista.
a.reverse()
print(a)

# Cuenta cuantas veces aparece el 4.
print(a.count(4))

# Borra toda la lista y equivale a a[:].
a.clear()
print(a)