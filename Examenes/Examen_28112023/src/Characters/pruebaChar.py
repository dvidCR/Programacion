import pygame
import sys
import random
 
# Inicializar Pygame
pygame.init()
 
# Configuración de la ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Color Change Example")
 
# Definir colores
white = (255, 255, 255)
 
# Clase para el sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Tamaño del sprite
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)  # Posición inicial del sprite
        self.color_change_timer = 0
 
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.change_color()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.change_color()
        if keys[pygame.K_UP]:
            self.rect.y -= 5
            self.change_color()
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
            self.change_color()
 
    def change_color(self):
        # Cambiar de color cada 15 frames (1/4 de segundo a 60 FPS)
        if self.color_change_timer <= 0:
            self.image.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.color_change_timer = 15
        else:
            self.color_change_timer -= 1
 
# Crear grupos de sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
 
# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    # Lógica de actualización
    all_sprites.update()
 
    # Limpiar pantalla
    screen.fill((0, 0, 0))
 
    # Dibujar sprites
    all_sprites.draw(screen)
 
    # Actualizar pantalla
    pygame.display.flip()
 
    # Controlar la velocidad de actualización
    clock.tick(60)