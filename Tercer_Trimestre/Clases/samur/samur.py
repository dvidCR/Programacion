import pandas as pd
from bbdd import BBDD

class samur(BBDD):
    
    def __init__(self, bbdd):
        super().__init__()
        self.connect(bbdd)
        self.csv = pd.read_csv("./activaciones_samur_2023.csv", delimiter=";")
        
    def sacarDatos(self):
        self.datos = []
        self.filas, self.columns = self.csv.shape
        for values in self.csv.values:
            self.insert(values[0], values[1], values[2], values[3], values[4], values[5], values[6])
            
            
        
if __name__ == "__main__":
    s = samur("samur")
    s.sacarDatos()