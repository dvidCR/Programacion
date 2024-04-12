import numpy

arr_txt = numpy.loadtxt("./arr.txt")
print(arr_txt)
print(arr_txt.dtype)

arr_csv = numpy.genfromtxt('./Hurricanes.csv', delimiter = ';')
print(arr_csv)