from collections import UserList

class Lista(UserList):
    def append(self, item):
        print("Se está agregando un elemento a la lista: ", item)
        # Llamar al método append de la clase base para agregar el elemento
        super().append(item)
        
    def pop(self, item = -1):
        print("Se está cogiendo el último elemento de la lista")
        return super().pop(item)
        
    def remove(self, item):
        print("Se está eliminando un elemento de la lista: ", item)
        super().remove(item)

l = Lista([1, 2, 3])

l.append(50)
print(l)

pop = l.pop()
print(f"Se ha cogido {pop}")
print(l)

l.append(pop)
print(l)

l.remove(50)
print(l)