'''
fichero = open("./texto.txt", "w")
fichero.write("1\n2\n3\n4\n\n5\n6\n7\n8\n9\n10")

fichero1 = open("./texto.txt", "r+")

for i in fichero1.readlines():
    print(i)
    
fichero1.close()
    
#print(fichero.readlines())

fichero2 = open("./texto.txt", "w+")

fichero2.write("oweifheoufnoeoifeiofefifeifneifn k fu e iueh few+ e\nw foieoineogibwgeouebogeobebeo \nefgnegnegign  g  gr gr g r g  gr g\n")
for i in fichero2.readlines():
    print(i)
    
    
fichero2.close()

fichero3 = open("./texto.txt", "a+")

fichero3.write("\n Hola mon señor")
for i in fichero3.readlines():
    print(i)
    
    
fichero3.close()
'''
imagen = open("./descarga.jpg", "rb")
for i in imagen.read():
    print(i)

imagen.close()