class Punto:
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def _get_radio(self):
        print(self.__x, self.__y)
    
    def _set_radio(self, x, y):
        self.__x = x
        self.__y = y
        
    radio = property(
        fget = _get_radio,
        fset = _set_radio
    )
    
p = Punto(1,2)
p._get_radio()
p._set_radio(5, 6)
p._get_radio()
