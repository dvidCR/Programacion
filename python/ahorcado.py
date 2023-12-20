import random

def obtener_palabra_aleatoria():
    palabras = ["amistad", "tecnologia", "musica", "deporte", "escuela", "examen", "vacaciones", "amor", "adolescencia"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def jugar_ahorcado():
    intentos_maximos = 6
    letras_adivinadas = []
    
    palabra_oculta = input("Ingresa la palabra oculta (o presiona Enter para una palabra aleatoria): ")
    
    if not palabra_oculta:
        palabra_oculta = obtener_palabra_aleatoria()
    
    while True:
        letra_usuario = input("\nIngresa una letra: ").lower()

        if letra_usuario.isalpha() and len(letra_usuario) == 1:
            if letra_usuario in letras_adivinadas:
                print("Ya has ingresado esa letra. Intenta con otra.")
            else:
                letras_adivinadas.append(letra_usuario)
                tablero = mostrar_tablero(palabra_oculta, letras_adivinadas)
                print(tablero)

                if tablero.replace(" ", "") == palabra_oculta:
                    print("\n¡Felicidades! Has adivinado la palabra.")
                    break

                if letra_usuario not in palabra_oculta:
                    intentos_maximos -= 1
                    print(f"Incorrecto. Te quedan {intentos_maximos} intentos.")

                    if intentos_maximos == 0:
                        print(f"\n¡Oh no! Te has quedado sin intentos. La palabra era: {palabra_oculta}")
                        break
        else:
            print("Por favor, ingresa una letra válida.")

if __name__ == "__main__":
    print("¡Bienvenido al juego de ahorcado!")
    jugar_ahorcado()
