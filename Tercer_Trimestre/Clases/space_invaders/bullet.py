import pygame
from pygame.sprite import Sprite
from ship import Ship

class Bullet(Sprite, Ship):
    
    def __init__(self, ai_game):
        """ Crear la bala donde está la nave """
        super().__init__()
        self.ship = ai_game.ship
        self.bullets = pygame.sprite.Group()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crear la bala en el rect (0, 0) .
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)
        
    def update(self):
      """Move the bullet up the screen."""
      # Update the exact position of the bullet.
      self.y -= self.settings.bullet_speed

      # Update the rect position.
      self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
      