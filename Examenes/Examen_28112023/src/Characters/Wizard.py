from Characters.BasicCharacter import BasicCharacter
from Arms.BasicArm import BasicArm
import pygame

class Wizard(BasicCharacter):
    
    def __init__(self):
        super().__init__()
        
        self.WizardX = 30
        self.WizardY = 30
        self.barraMX = 750
        self.barraMY = 10
        self.mana = 40
    
    def movements(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RSHIFT]:
            if self.mana > 0:
                self.bullets.append(BasicArm(self.WizardX + self.width // 2, self.WizardY, 80))
                self.mana-=1
                self.barraMX+=1
        elif self.mana < 40:
            self.mana+=1
            self.barraMX-=1
        return super().update()
        
    def character(self):
        BasicCharacter(pygame.draw.rect(self.screen, self.colorWi, pygame.Rect(self.WizardX, self.WizardY, 10, 20)))
     
    def magia(self):
        pygame.draw.rect(self.screen, self.colorM, pygame.Rect(self.barraMX, self.barraMY, self.mana, 20))