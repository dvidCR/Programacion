valor = 0
suma = 0
while (suma < 10):
    suma+=1
    valor = valor + suma
print(valor)

for suma in range(1,11):
    valor = valor + suma
    
print(valor)


#Esto es una potencia
valor = 2
lista=[]
for i in range(1,11):
    lista.append(valor ** i)
print(lista)

par = 0
impar = 1
for i in range(1,245,2):
    par = par + i
print("Par: " + str(par))
for i in range(1,245,1):
    impar = impar + i
print("Impar: " + str(impar))