import numpy

# Ejercicio 1: Ejercicio 1: Crea un array de una dimensión. (Vector)
print(numpy.arange(5))

# Ejercicio 2: Crea un array de dos dimensiones. (Array)
print(numpy.arange(4).reshape(2,2))

# Ejercicio 3: Hacer lo mismo que en los dos anteriores pero ahora usando la siguiente lista.
lista = [1, 11, 111, 1111]
print(numpy.array(lista))
print(numpy.array(lista).reshape(2,2))

# Ejercicio 4: Crea un array 5x5 de zeros.
print(numpy.zeros(25).reshape(5,5))

# Ejercicio 5: Crea un vector cuyo límite inferior sea 0 y el límite superior sea 20 y 
# tenga 5 elementos comprendidos en ese intervalo que sean literalmente iguales.

print(numpy.linspace(start=0, stop=20, num=5))

# Ejercicio 6: Crea un array de 8 elementos de 2x2x2 de ceros. (Tensor)
print(numpy.zeros(8).reshape(2,2,2))

# Ejercicio 7: Crea un array que vaya de 2 al 20 y obten el elememnto de la posición 7.
ej7 = numpy.array(range(2, 21))
print(ej7[7])

# Ejercicio 8: crea un vector de 20 elementos y mediante el método slice() crea otro vector a partir del 
# vector de 20 elementos que empiece en 1, termine en 10 y tenga los números de dos en dos.
ej8 = numpy.arange(20)
s = slice(1, 10, 2)
print(ej8[s])

# Ejercicio 9: Explica el siguiente código.
arr7 = numpy.arange(20)
print(arr7[2:])
# Crea un vector de 20 elementos el cual empieza después de los dos primero elementos del vector.

# Ejercicio 10: Utilizando lo anterior a partir del arr7 quiero obtener una lista que va de 0 a 15.
print(arr7[:16])

# Ejercicio 11: Crea un array de ceros de 3x3. A partir de ese array prueba el 
# atributo shape, ndim, y itemsize. Explica que nos dicen estos atributos sobre la estructura
ej11 = numpy.arange(9).reshape(3,3)
print(ej11.shape) # Nos muestre las dimensoniones del array.
print(ej11.ndim) # Devuelve el numero de dimensoiones del array (1: es un vector, 2: es un array, 3: es un tensor).
print(ej11.itemsize) # Nos devuelve el tamaño del array en bytes.