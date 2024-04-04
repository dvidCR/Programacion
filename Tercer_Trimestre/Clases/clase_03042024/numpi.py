import numpy
import matplotlib.pyplot as plt

# numpy
vector = numpy.arange(5)
print(vector)

matriz = numpy.arange(9).reshape(3,3)
print(matriz)

tensor = numpy.arange(12).reshape(3,2,2)
print(tensor)

# arrays
arr = numpy.array([1,2,3,4,5,6])
print(arr)

arr2 = numpy.array([[1,2], [1,2]])
print(arr2)

# arrays con secuencias
print(numpy.arange(start=2, stop=10, step=1))
print(numpy.arange(start=2, stop=10, step=2))
print(numpy.arange(start=20, stop=10, step=-1))

# uso de linspace
print(numpy.linspace(start=1, stop=10, num=10))
print(numpy.linspace(start=1, stop=10, num=20))

# crear lista con 0
print(numpy.zeros(9))
print(numpy.zeros([2,2]))

# ahora con 1
print(numpy.ones(9))
print(numpy.ones([2,2]))

# otra manera de hacer una matriz
print(numpy.full(shape=(2,2), fill_value=5))

# ----------------------------------------------------------------------------------------

x = numpy.linspace(0,3,20)
y = numpy.linspace(0,9,20)

plt.plot(x,y)
plt.show()

# ----------------------------------------------------------------------------------------

# un vector aleatorio
print(numpy.random.rand(2,2))

# grafico de calor
x = numpy.random.rand(30,30)
plt.imshow(x, cmap=plt.cm.hot)
plt.colorbar()
plt.show()

# grafico 3D
from mayavi import mlab

mlab.surf(x)
mlab.axes()
mlab.show()

# hay que crear un vector de ceros de tamaño 10 y que la quinta posicion sea un 1
ej = numpy.zeros(10)
ej[4] = 1
print(ej)