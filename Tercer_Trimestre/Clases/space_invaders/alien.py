import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  
    def __init__(self, ai_game):
    
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Cargamos la imagen de los alien.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # Lo vamos a situar arriba del todo de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # La posición de los alines es muy exacta por tanto la vamos a crear como un número con decimales para ser más precisos
        self.x = float(self.rect.x)
    
    def update(self):
        # mueve a la derecha el alien
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
