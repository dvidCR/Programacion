import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
from gameStats import GameStats
from pygame.sprite import Group

class AlienInvasion:
    
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """CONSTRUCTOR DEL JUEGO DONDE INICIALIZAMOS LAS VARIABLES MÁS IMPORTANTES."""
        pygame.init()
        self.game_active = True
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Invasión alieligena")
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Create an instance to store game statistics.
        self.stats = GameStats(self)


    def run_game(self):
        """BUCLE PRINCIPAL DEL JUEGO"""
        while True:
            self._check_events()
            if self.game_active:
                self._check_events()
                self.limits()
                self.ship.size()
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._update_screen()
                self.clock.tick(60)
            
            
    def _check_events(self):
        """método que responde a los eventos que se producen en la pantalla del juego"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_left = False
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_right = False
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            """ Creamos el objeto bala y lo añadimos al grupo."""
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
                
    def _update_screen(self):
        """Actualiza las imágenes de pantalla y pinta la nueva pantalla."""
        # flip() es eñ emcargadp de dibujar los elementos del juego
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
    
    def _update_bullets(self):
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
                
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            # AÑADE ESTA LÍNEA DESPUÉS DEL SELF._SHIP_HIT()
            self._check_aliens_bottom()
        
    def limits(self):
        # Limita el margen derecho
        if self.ship.rect.x > self.settings.screen_width - self.ship.image_ship_witdh:
            self.ship.rect.x = self.settings.screen_width - self.ship.image_ship_witdh

        # Limita el margen izquierdo
        if self.ship.rect.x < 0:
            self.ship.rect.x = 0
            
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # finzaliza la línea
            current_x = alien_width
            current_y += 2 * alien_height
                        
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
        
    def _check_fleet_edges(self):
        """Si detecta un borde los alines cambia la dirección"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Cambio de la dirección"""
        for alien in self.aliens.sprites():
            if(alien.rect.y > self.ship.rect.y):
                alien.rect.y += self.settings.fleet_drop_speed
                print(alien.rect.y)
            else:
                self.aliens.remove()
                self.game_active = False
        self.settings.fleet_direction *= -1
        
    def _check_bullet_alien_collisions(self):
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            
    
    def _ship_hit(self):
        """ La nave ha sido alcanzada """
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1

            # no tienes balas y reseteas
            self.bullets.empty()
            self.aliens.empty()

            # nueva posición
            self._create_fleet()
            self.ship.center_ship()

        # Pause.
            sleep(0.5)
        else:
            self.game_active = False
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break



if __name__ == '__main__':
# Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()