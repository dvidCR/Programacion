import pygame

class BasicArm:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity

    def draw(self, screen):
        #if disparo == "mago":
            pygame.draw.rect(screen, (128, 0, 128), (self.x, self.y, 15, 2)),
        