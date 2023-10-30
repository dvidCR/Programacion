import math

class Point:
    '''
        Creamos una clase para mostrar las coordenadas
    '''
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0
    
    def move(self,point):
        lesx =(self.x - point.x)**2
        lesy = (self.y - point.y)**2
        return math.sqrt(lesx + lesy)

point1 = Point(14,30)

point2 = Point(50,1)

print(point1.move(point2))