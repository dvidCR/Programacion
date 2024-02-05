class ejercicio:
    
    def __init__(self):
        pass
    
    def calc(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
            return "hola"
        else:
            return n
        
    def calc2(self, a, b):
        try:
            return a/b
        except Exception as a:
            print(f'Error: {a}')
            return "alerta por subnormal"
        
    def error3 (self):
      
        try:
            lista = [1, 2, 3]
            print(lista[3])
        except IndexError as e:
            print(f"Error de índice: {e}")
        except Exception as e:
            print(f"Otro error: {e}")
            
    def error4(self):
        
        try: 
            numero = int(input("Ingresa un número: ")) 
        except ValueError: 
            print("Eso no es un número válido.") 
        else: 
            print(f"Has ingresado el número {numero}") 
        finally: 
            print("Fin del bloque try-except")

class MiError(Exception): 
    
    pass

try: 
    raise MiError("¡Algo salió mal!") 
except MiError as e: 
    print(f"Mi error dice: {e}")
    
'''
e = ejercicio()
res = e.error4()
print("El resultado es " + str(res))
'''