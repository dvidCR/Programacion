import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion(Settings, Ship):
    
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """CONSTRUCTOR DEL JUEGO DONDE INICIALIZAMOS LAS VARIABLES MÁS IMPORTANTES."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Invasión alieligena")
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)

    def run_game(self):
        """BUCLE PRINCIPAL DEL JUEGO"""
        while True:
            # print(self.ship.rect.x)
            self._check_events()
            self.limits()
            self.ship.size()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            
            
    def _check_events(self):
        """método que responde a los eventos que se producen en la pantalla del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            else:
                self.ship.moving_left = False
                self.ship.moving_right = False
                
            if event.type == pygame.K_SPACE:
                    self.ship.draw()
                
    def _update_screen(self):
        """Actualiza las imágenes de pantalla y pinta la nueva pantalla."""
        # flip() es eñ emcargadp de dibujar los elementos del juego
        pygame.display.flip()
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
    def limits(self):
        # Limita el margen derecho
        if self.ship.rect.x > self.settings.screen_width - self.ship.image_ship_witdh:
            self.ship.rect.x = self.settings.screen_width - self.ship.image_ship_witdh

        # Limita el margen izquierdo
        if self.ship.rect.x < 0:
            self.ship.rect.x = 0
        

if __name__ == '__main__':
# Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()