from collections import Counter 

# Ejercicio 1
p = Counter("Hola que tal estas in amet".split())
print(p)

# Ejercicio 2
with open("./fichero.txt", "r") as f:
    print(Counter(f.read().split()))
    
# Ejercicio 3
with open("./fichero.txt", "r") as f:
    c = Counter(f.read().split())
    print(f"in: {c.get('in')}")
    
# Ejercicio 4
c = Counter("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum".split())
for i in c:
    print(f"{i}: {c.get(i)}")
    
# Ejercicio 5
with open("./fichero.txt", "r") as f:
    print(Counter(f.read().split()).most_common(1))
    
# Ejercicio 6
print(p + c)