class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("La temperatura marcada no se puede mostrar")
        self._celsius = valor
    
temp = Temperatura(25)
print(temp.celsius)
try:
    temp.celsius = -500
    print(temp.celsius)
except ValueError as e:
    print(e)