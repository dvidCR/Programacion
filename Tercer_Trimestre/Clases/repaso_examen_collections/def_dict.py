from collections import defaultdict

l = [("MADRID", "M"), ("SALAMANCA", "SA"), ("BARCELONA", "B"), ("BURGOS", "BA"), ("SEVILLA", "S")]
d = defaultdict(list)

for i in l:
    d[i[0]].append(i[1])
    
print(d)

# Un Counter pero con defaultdict
di = defaultdict(int)
with open("./fichero.txt", "r") as f:
    r = f.read().split()
    for i in r:
        di[i] += 1
        
print(di)