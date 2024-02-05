import os

# A este if ni caso es para hacer que el script funcione donde yo quiero
if os.getcwd() != "D:\Clase\Programacion\Programacion\python\ejercico_01022024":
    os.chdir("D:\Clase\Programacion\Programacion\python\ejercico_01022024")

try:
    os.mkdir("virus")
except:
    pass

os.chdir("virus")

for i in range (0,3):
    with open("file"+str(i)+".txt","w") as g:
        g.write("Mira que bonito, un pajaro")
        
for i in os.listdir():
    x = i.split(".")
    if x[1] == "txt":
        with open(i ,"w") as vi:
            vi.write("Infectado!!")