from Characters.Character import Character
from Arms.BasicArm import BasicArm
import pygame

class Wizard(Character):
    
    def __init__(self, screen, x=30, y=30, Wix=30, Wiy=30, Wax=50, Way=50, posxM=750, posyM=10, posxF=700, posyF=10, direction='right', velocity=10):
        super().__init__(screen, x, y, Wix, Wiy, Wax, Way, posxM, posyM, posxF, posyF, direction, velocity)
    
        self.mana = 40
    
    def movements(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RSHIFT]:
            if self.mana > 0:
                self.bullets.append(BasicArm(self.Wix + self.width // 2, self.Wiy, 80))
                self.mana-=1
                self.posxM+=1
        elif self.mana < 40:
            self.mana+=1
            self.posxM-=1
        return super().movements()
        
    def character(self):
        pygame.draw.rect(self.screen, self.colorWi, pygame.Rect(self.Wix, self.Wiy, 10, 20))
     
    def magia(self):
        pygame.draw.rect(self.screen, self.colorM, pygame.Rect(self.posxM, self.posyM, self.mana, 20))