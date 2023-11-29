from Characters.Character import Character
from Arms.BasicArm import BasicArm
import pygame

class Warrior(Character):
    
    def __init__(self, screen, x=30, y=30, Wix=30, Wiy=30, Wax=50, Way=50, posxM=750, posyM=10, posxF=700, posyF=10, direction='right', velocity=10):
        super().__init__(screen, x, y, Wix, Wiy, Wax, Way, posxM, posyM, posxF, posyF, direction, velocity)
    
        self.fuerza = 40
    
    def movements(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            if self.fuerza > 0:
                self.bullets.append(BasicArm(self.Wax + self.width // 2, self.Way, 80)) 
                self.fuerza-=1
                self.posxM+=1
        elif self.fuerza < 40:
            self.fuerza+=1
            self.posxM-=1
        return super().movements()
        
    def character(self):
        pygame.draw.rect(self.screen, self.colorWa, pygame.Rect(self.Wax, self.Way, 10, 20))
     
    def barra(self):
        pygame.draw.rect(self.screen, self.colorF, pygame.Rect(self.posxF, self.posyF, self.fuerza, 20))