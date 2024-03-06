lista = [12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]

resultado = {}

for i in range(0, len(lista)):
    if (lista[i] in resultado.keys()):
        resultado[lista[i]] = resultado[lista[i]] + 1
    else:
        resultado.update({lista[i]: 1})
        
print(resultado)