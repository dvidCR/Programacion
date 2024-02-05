coche1 = {
    "Marca": "Ford",
    "Modelo": "Mustang"
}
coche2 = {
    "Marca": "Mercedes",
    "Modelo": "GLE"
}
coches = [coche1, coche2]
pregunta = input("¿Quieres ver la Marca, el Modelo o Todo?: ")
if (pregunta == "Todo"):
    print (coches)
else:
    for i in coches:
        print (i[pregunta])