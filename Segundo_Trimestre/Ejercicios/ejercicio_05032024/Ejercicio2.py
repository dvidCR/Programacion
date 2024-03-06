nombres = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5}

lista = []

for i in range(0, len(nombres.values())):
    if (nombres.values() not in lista):
        lista.append(nombres)
    
print(lista)