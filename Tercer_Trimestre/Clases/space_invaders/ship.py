import pygame
import cv2

class Ship:
    """Clase que gestiona la nave."""
    
    def __init__(self, ai_game):
    
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.moving_left = False
        self.moving_right = False
        self.image_ship_witdh = 0
        self.image_ship_height = 0
    
    # Cargamos la imagen de la imagen y la asociamos a un rectángulo para que sea más fácil gestionar
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
    # Posicionamos la nave en la mitad de fondo de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
    
    def size(self):
        self.image_ship = cv2.imread("images/ship.bmp")
        self.image_ship_height, self.image_ship_witdh, _ = self.image_ship.shape
        print(self.image_ship_witdh)
    
    def blitme(self):
        """Dibuja la nave en la posición actual."""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        # actualiza el movimiento de la nave dependiendo si la variable right es true
        if self.moving_right:
            self.rect.x += 3
        elif self.moving_left:
            self.rect.x -= 3
    
    def draw(self):
        puntos_poligono = [(50, 90), (70, 50), (250, 120), (320, 250), (150, 300)]
        pygame.draw.polygon((50,50), (0, 255, 0) ,puntos_poligono)