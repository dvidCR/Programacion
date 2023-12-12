import pygame

pygame.init()

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        super().__init__()
        
        self.width = width
        self.height = height
        
        self.image = pygame.Surface([width,height])
        self.image.fill("red")
        
        self.rect = self.image.get_rect()
        
    def update(self):
        keys = pygame.key.get_pressed()
        
        if keys == [pygame.K_w]:
            self.rect.y -= 5
        if keys == [pygame.K_a]:
            self.rect.x -= 5
        if keys == [pygame.K_s]:
            self.rect.y += 5
        if keys == [pygame.K_d]:
            self.rect.x += 5
   
sprite = Sprite(30, 60)
sprites = pygame.sprite.Group()
sprites.add(sprite)

screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True

while (running == True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    sprites.update()

    screen.fill("black")

    sprites.draw(screen)

    pygame.display.flip()
    
    clock.tick(60)  # Limita a 60 FPS
    
pygame.quit()