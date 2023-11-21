class Edifico:
    
    def __init__(self, tipo, capacidad, coste):
        self.tipo = tipo
        self.capacidad = capacidad
        self.coste = coste
        
class Casa(Edifico):
    
    def __init__(self, tamaño, plantas, valorZona, salas):
        self.tamaño = tamaño
        self.plantas = plantas
        self.valorZona = valorZona
        self.salas = salas
        
    def caracteristicas(self):
        self.tipo = "Chalet"
        self.capacidad = "4 personas"
        self.coste = 80000
        self.tamaño = "160 x 100"
        self.plantas = 2
        self.valorZona = "Media"
        self.salas = "4 habitaciones, 2 baños, 1 cocina, 1 comedor, 1 garaje"
        
class Granja(Edifico):
    
    def __init__(self, tamaño, tipoParcela):
        self.tamaño = tamaño
        self.tipoParcela = tipoParcela
        
    def caracteristicas(self):
        self.tipo = "Establo"
        self.capacidad = "80 vacas aporx."
        self.coste = 60000
        self.tamaño = "175 x 120"
        self.tipoParcela = "Ganado"
        self.valorZona = "Bajo"
        self.salas = "1 almacen, 1 corral amplio"
        
class Barraca(Edifico):
    
    def __init__(self, tamaño, parcela, plantas, equipo):
        self.tamaño = tamaño
        self.parcela = parcela
        self.plantas = plantas
        self.equipo = equipo
                
    def caracteristicas(self):
        self.tipo = "Barraca"
        self.capacidad = "1 o 2 personas"
        self.coste = 10000
        self.tamaño = "100 x 60"
        self.parcela = "De regadio"
        self.plantas = 1
        self.equipo = "Semillas de cereal"