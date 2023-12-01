import pygame
import sys
from Arms.BasicArm import BasicArm
 
# Inicializar Pygame
pygame.init()
 
# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Color Change Example")
 
# Clase para el sprite
class BasicCharacter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 20))  # Tamaño del sprite
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)  # Posición inicial del sprite
        self.image.fill("purple")
        self.bullets = []
 
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_SPACE]:
            if self.fuerza > 0:
                self.bullets.append(BasicArm(self.Wax + self.width // 2, self.Way, 80))
            
    def bullets(self):
        for bullet in self.bullets[:]:
            bullet.update()
            bullet.draw(self.screen)
            if bullet.x > 800 or bullet.x < 0:
                self.bullets.remove(bullet)
            
            
# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
player = BasicCharacter()
all_sprites.add(player)
 
# Bucle principal
clock = pygame.time.Clock()

 
# Lógica de actualización
all_sprites.update()


# Dibujar sprites
all_sprites.draw(screen)

# Actualizar pantalla
pygame.display.flip()

# Controlar la velocidad de actualización
clock.tick(60)