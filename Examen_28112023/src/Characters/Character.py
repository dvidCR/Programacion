import pygame
from Arms.BasicArm import BasicArm

class Character ():
    
    '''
    Tiene que tener unas coordenadas de inicio
    un personaje se puede mover
    un personaje tiene una representación 
    un personaje puede tener sprite y se puede gestionar desde aquí
    
    '''
    
    def __init__(self,screen, x=30, y=30, Wix=30,Wiy=30, Wax=50,Way=50, posxM=750, posyM=10, posxF=700, posyF=10 ,direction='right', velocity = 10):
        self.screen = screen
        self.x = x
        self.y = y
        self.Wix = Wix
        self.Wiy = Wiy
        self.Wax = Wax
        self.Way = Way
        self.posxM = posxM
        self.posyM = posyM
        self.posxF = posxF
        self.posyF = posyF
        self.sinMana = "Te has quedado sin mana"
        self.width = 10
        self.height = 20
        self.direction = direction
        self.velocity = velocity
        self.colorWi =   (0,0,200)
        self.colorWa = (255,0,0)
        self.colorM = (0,0,200)
        self.colorF = (255,0,0)
        self.black = (255,255,255)
        self.bullets = []
        #self.draw()
        
    def movements(self):
        
        # Obtener teclas presionadas
        
        keys = pygame.key.get_pressed()
            

        # Mover el mago
        if keys[pygame.K_LEFT]:
            self.Wix -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.Wix += self.velocity
        if keys[pygame.K_UP]:
            self.Wiy -= self.velocity
        if keys[pygame.K_DOWN]:
            self.Wiy += self.velocity
        
        # Mover el guerrero
        if keys[pygame.K_a]:
            self.Wax -= self.velocity
        if keys[pygame.K_d]:
            self.Wax += self.velocity
        if keys[pygame.K_w]:
            self.Way -= self.velocity
        if keys[pygame.K_s]:
            self.Way += self.velocity
        
         # Disparar balas
                          
        for bullet in self.bullets[:]:
            bullet.update()
            bullet.draw(self.screen)
            if bullet.x > 800 or bullet.x < 0:
                self.bullets.remove(bullet)

        # limits--> Hay que crear clases que controlen los límites del mapa o bien añadirlo al mapa
        #TODO: configurar height and with
        #self.x = max(0, min(self.x, 10 - 5))
        #self.y = max(0, min(self.y, 20 - 5))
        #print (self.Wix)
        #print (self.Wiy)
        #print (self.Wax)
        #print (self.Way)
        # draw the new position

        # disply update after movements
        pygame.display.flip()
        pygame.time.delay(30) 
        
    # basic rectangle element in screen with movements  
    def draw (self):
        
       #size by while this!!
       
       pass

