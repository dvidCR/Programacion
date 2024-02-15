class Vehiculo:
    
    #Creo los metodos privados para que no puedan ser modificados a placer desde fuera
    def __init__(self, marca, modelo, matricula, añoFabricacion):
        self.__marca = marca
        self.__modelo = modelo
        self.__matricula = matricula
        self.__añoFabricacion = añoFabricacion
     
    def _getVehiculo(self): 
        return f"El vehiculo con la marca {self.__marca} y su modelo {self.__modelo} con matricula {self.__matricula} y su año de frabicación es el {self.__añoFabricacion}"
    
    #He puesto un mathc en el setter para evitar tener una buena cantidad de los mismos 
    def _setVehiculo(self, escoger, mod):
        match escoger:
            case 1:
                self.__marca = mod
                
            case 2:
                self.__modelo = mod
                
            case 3:
                self.__matricula = mod
                
            case 4:
                self.__añoFabricacion = mod
    
    #Tanto el getter como el setter los he puesto protegidos para que solo se usen cuando yo lo diga
            
    vehiculo = property(
        fget = _getVehiculo,
        fset = _setVehiculo
    )
    
v = Vehiculo("Seat", "Leon", "0228VJH", "02/02/2022")
print(v._getVehiculo())

escoger = int(input("¿Que quieres modificar?:\n 1. Marca\n 2. Modelo\n 3. Matricula\n 4. Año de Fabricacion\n: "))
mod = input("Que quires modificar: ")

v._setVehiculo(escoger, mod)
print(v._getVehiculo())