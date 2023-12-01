from Characters.Character import Character
from Arms.BasicArm import BasicArm
import pygame

class Warrior(Character):
    
    def __init__(self, screen, x=30, y=30, WizardX=30, WizardY=30, Wax=50, Way=50, barraMX=750, barraMY=10, barraFX=700, barraFY=10, direction='right', velocity=10):
        super().__init__(screen, x, y, WizardX, WizardY, Wax, Way, barraMX, barraMY, barraFX, barraFY, direction, velocity)
    
        self.fuerza = 40
    
    def movements(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            if self.fuerza > 0:
                self.bullets.append(BasicArm(self.Wax + self.width // 2, self.Way, 80))
                self.fuerza-=1
                self.barraMX+=1
        elif self.fuerza < 40:
            self.fuerza+=1
            self.barraMX-=1
        return super().movements()
        
    def character(self):
        pygame.draw.rect(self.screen, self.colorWa, pygame.Rect(self.Wax, self.Way, 10, 20))
     
    def barra(self):
        pygame.draw.rect(self.screen, self.colorF, pygame.Rect(self.barraFX, self.barraFY, self.fuerza, 20))