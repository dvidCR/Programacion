import collections

'''c1 = collections.Counter(a=3, b=4, c=6)

# Ejercicio 1
print(list(c1.elements()))
            

# Ejercicio 2  
frase = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor"
c2 = collections.Counter(frase.split())
print(c2.most_common())'''

# Ejercico 3

with open("./el_quijote.txt", "r", encoding="utf-8") as q:
    c3 = collections.Counter(q.read().split())
    print(c3.most_common(30))
    
    
# Ejercico 4
from collections import defaultdict

frase = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor"
word_counts = defaultdict(int)
for word in frase:
    word_counts[word] += 1
    
print(word_counts)

with open("./el_quijote.txt", "r", encoding="utf-8") as q:
    word_counts = defaultdict(int)
    for word in q.read().split():
        word_counts[word] += 1
        
    print(word_counts)