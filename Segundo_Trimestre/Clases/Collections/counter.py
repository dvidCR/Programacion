from collections import Counter

# Uso de Counter
c = Counter("abcabadecba")
print(c)
# Resultado: Counter({'a': 4, 'b': 3, 'c': 2, 'd': 1, 'e': 1})


# Con esto eliminamos una letra del contador
del c['a']
print(c)
# Resultado: Counter({'b': 3, 'c': 2, 'd': 1, 'e': 1})


# Actulizar el Counter(también vale para actualizar una lista), no sobrescibe
c.update("axcqq")
print(c)
# Resultado: Counter({'b': 3, 'c': 3, 'q': 2, 'd': 1, 'e': 1, 'a': 1, 'x': 1})


# También podemos pedrle que nos cuente cuantas veces se repite una cosa en concreto
print(c["c"]) # Resultado: 3
print(c["y"]) # Resultado: 0


# Al contador(que funciona como una lista) podemos añadirle variables y, obviamente, el nombre de las variables
# no se pueden repetir
c1 = Counter(a=13, b=15, c=0)
print(c1)
# Resultado: Counter({'b': 15, 'a': 13, 'c': 0})


# EL metodo elements lo que hace es repetir cuantas veces haya una letra, en este caso como 
# puedes ver va a poner 13 veces 'a' porque 'a': 13
# Otra cosa importante es que siempre lo tienes que ordenar porque si no lo haces solo te mostrara la
# direccion de memoria
print(sorted(c1.elements()))
print(sorted(c.elements()))
print(c1.elements())
# Resultado: ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
# Resultado: ['a', 'b', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'q', 'q', 'x']
# Reusltado: itertools.chain object at 0x000001BE9AA2B8E0>


# El metodo most_common, como bien su nombre dice, solo muestra los más comunes
# Dentro de los parentesis también puedes poner por ejemplo los tres más comunes, o los cinco más comunes
print(c.most_common())
print(c.most_common(3))
print(c.most_common(5))
# Resultado: [('b', 3), ('c', 3), ('q', 2), ('d', 1), ('e', 1), ('a', 1), ('x', 1)]
# Resultado: [('b', 3), ('c', 3), ('q', 2)]
# Resultado: [('b', 3), ('c', 3), ('q', 2), ('d', 1), ('e', 1)]


# Ahora para poder restar los valores iguales de dos contadores distintos tenemos que usar el subtract
r1 = Counter(a=4, b=2, c=0, d=-2)
r2 = Counter(a=1, b=2, c=3, d=4)
r1.subtract(r2)
print(r1)
# Resultado: Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})


# Para sacar la suma total de todo tendriamos que usar el metodo total
t = Counter(a=10, b=5, c=0)
print(t.total())
print(c1.total())
print(c.total())
# Resultado: 15
# Resultado: 28
# Resultado: 12


# Tabién se puede utilizar complementandolo con formkey que me crea valores a un diccionario por defecto(el por
# defecto en este caso es el 0)
f = dict.fromkeys(['a', 'b', 'c'], 0)
c2 = Counter(f)
print(c2)
# Resultado: Counter({'a': 0, 'b': 0, 'c': 0})


# Con el método clear borramos absolutamente todo
c.clear()
print(c)
# Resultado: Counter()

# Con el list listamos todos los elementos pero sin repetirlos
print(list(c1))
# Resultado: ['a', 'b', 'c']


#Con el set seria lo mismo que con el list pero sin transfromarlo en una lista
print(set(c1))
# Resultado: {'b', 'c', 'a'}


# Con el dicto lo que hacemos es convertirlo todo en un diccionario
print(dict(c1))
# Resultado: {'a': 13, 'b': 15, 'c': 0}


# Con el items creamos una lista separando los elementos y el contador ej:[('a', 12)]
print(c1.items())
# Resultado: dict_items([('a', 13), ('b', 15), ('c', 0)])


# También podemos hacer operaciones e igualaciones entre contadores
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)

sum = c + d
print(sum)
# Resultado: Counter({'a': 4, 'b': 3})

res = c - d
print(res)
# Resultado: Counter({'a': 2})

min = c & d
print(min)
# Resultado: Counter({'a': 1, 'b': 1})

max = c | d
print(max)
# Resultado: Counter({'a': 3, 'b': 2})

eq = c == d
print(eq)
# Resultado: False

gt_lt = c <= d
print(gt_lt)
# Resultado: False