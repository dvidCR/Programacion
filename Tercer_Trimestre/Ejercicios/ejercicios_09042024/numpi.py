import numpy

# Ejercicio 1
matriz = numpy.arange(9).reshape(3,3)
print(matriz)

# Ejercicio 2 
vector = numpy.array([1,2,0,0,3,4,0,5])
for i in range(len(vector)):
    if(vector[i] == 0):
        print(f"La posición {i} es un 0")
        
# Ejercicio 3
unos = numpy.ones(9).reshape(3,3)
print(unos)

# Ejercicio 4
lista = []
for i in range(0, 100):
    aleatorio = numpy.random.randint(0,9999)
    lista.append(aleatorio)
    
matriz = numpy.array(lista).reshape(10,10)
print(matriz)

# Ejercicio 5
matriz = numpy.zeros(25).reshape(5,5)
numpy.fill_diagonal(matriz, [1, 2, 3, 4])
print(matriz)