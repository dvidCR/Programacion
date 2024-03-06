l1 = [2,5,6,7,1]
l2 = [3,8,4,9,0]

l = l1 + l2

l.sort()

print(l)

biblioteca = {
    "titulo": "El Quijote",
    "ISBN": 65416541865,
    "autor": "Cervantes",
    "edicion": 1
}

# acceder a los datos de un diccionario
print(biblioteca["titulo"])
print(biblioteca.get("titulo"))

# añadir datos a un diccionario
biblioteca.update({"editorial": "VOX"})
print(biblioteca.get("editorial"))

# modificar datos en un diccionario
biblioteca["ISBN"] = 7894561230
print(biblioteca["ISBN"])
biblioteca.update({"ISBN": 1234567890})
print(biblioteca.get("ISBN"))

# devolver la lista en String
print(biblioteca.keys())
print(biblioteca.values())

# borrar seccions de un diccionario
print(biblioteca.pop("autor", "No encontrado"))
print(biblioteca.pop("autor2", "No encontrado"))

# devuelve un booleano si existe o no
print("Cervantes" in biblioteca.values())
print(1 in biblioteca.values())

# devuelve todo el contenido del diccionario
print(biblioteca)