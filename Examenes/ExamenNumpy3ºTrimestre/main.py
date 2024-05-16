import array
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Ejercicio1():
    notas = array.array("d", [])
    print("Notas")
    notas.append(comprobarNotas(int(input("¿Cuanto ha sacado el alumno en el primer examen?: "))))
    notas.append(comprobarNotas(int(input("¿Cuanto ha sacado el alumno en el segundo examen?: "))))
    notas.append(comprobarNotas(int(input("¿Cuanto ha sacado el alumno en el tercer examen?: "))))
    notas.append(comprobarNotas(int(input("¿Cuanto ha sacado el alumno en el cuarto examen?: "))))
    notas.append(comprobarNotas(int(input("¿Cuanto ha sacado el alumno en el quinto examen?: "))))
    
    alta = notas[0]
    for i in notas:
        if i > alta:
            baja = alta
            alta = i
        elif i < alta:
            baja = i
    
    media = (notas[0] + notas[1] + notas[2] + notas[3] + notas[4]) / len(notas)
      
    print(f"En el primer examen ha sacado un {notas[0]}\n\
        En el segundo examen ha sacado un {notas[1]}\n\
        En el tercer examen ha sacado un {notas[2]}\n\
        En el cuarto examen ha sacado un {notas[3]}\n\
        En el quinto examen ha sacado un {notas[4]}\n")
    print(f"La media del alumno es de {media}")
    print(f"La nota mas alta es {alta}\n")
    print(f"La nota mas baja es {baja}\n")
    
    
def comprobarNotas(nota):
    if nota > -1 and nota < 11:
        return nota
    else:
        print("Nota mal escrita")
        return None
    
def Ejercicio2():
    diagonal = np.zeros(25).reshape(5, 5)
    np.fill_diagonal(diagonal, [1])
    print(diagonal)
    
def Ejercicio3():
    csv = pd.read_csv("./AppleStore.csv", delimiter=",")
    filas, columns = csv.shape
    print(f"Nº de filas: {filas}\nNº de columnas: {columns}")
    
    csv.plot(kind="bar", title="Estadisticas de la Apple Store")
    plt.show()
    
    precioMedia = csv["price"].mean()
    tamañoMedia = csv["size_bytes"].mean()
    print(f"El precio medio es de {precioMedia} y el tamaño medio es de {tamañoMedia}")
    
    csv["track_name"].plot(kind="bar", title="Precio Medio", x="price")
    plt.show()
            
    csv["track_name"].plot(kind="bar", title="Tamaño Medio", x="size_bytes")
    plt.show()
    
    csv["size_bytes"].plot(kind="bar", title="Tamaño Medio", y=range(0, 5))
    plt.show()
    
if __name__ == "__main__":
    # Ejercicio1()
    # Ejercicio2()
    Ejercicio3()