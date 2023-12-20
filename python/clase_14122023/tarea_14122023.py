class Empleado:
    def __init__(self, salarioBase, bonos, nombre, apellido):
        self._salarioBase = salarioBase
        self._bonos = bonos
        self._nombre = nombre
        self._apellido = apellido
    
    @property
    def salarioBase(self):
        return self._salarioBase
    
    @salarioBase.setter
    def salarioBase(self, salarioBase):
        self._salarioBase = salarioBase
    
    
    @property
    def bonos(self):
        return self._bonos
    
    @bonos.setter
    def bonos(self, bonos):
        self._bonos = bonos
    
    @property
    def Email(self):
        return f"{self._nombre}@{self._apellido}.com"
    
    @property
    def salarioTotal(self):
        if self._salarioBase > 0:
            return self._salarioBase + self._bonos
        raise ValueError("La cifra que le has asignado no puede ser negativa")
    
    
try:
    emp = Empleado(-500, 5, "Carlos", "Martinez")
except ValueError as e:
    print(e)
print(emp.salarioTotal)
print(emp.Email)