class Punto:
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    @property
    def radioX(self):
        return self.__x
    
    @radioX.setter
    def set_radioX(self, x):
        self.__x = x
        
    @property
    def radioY(self):
        return self.__y
    
    @radioY.setter
    def set_radioY(self, y):
        self.__y = y
        
p = Punto(1,2)
p.radioX()
p.radioY()
p.set_radioX(5)
p.set_radioY(6)
p.radioX()
p.radioY()