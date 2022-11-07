import pygame

VELB = 6
VEL = 4

pygame.init()

#Classes dos cactos 
class Cacto(pygame.sprite.Sprite):
    def __init__(self, size, cx, cy):
        super().__init__()
        self.image = pygame.image.load("./sprites/enemy/trap.png")
        self.image = pygame.transform.scale(self.image, size)
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(bottomleft = (cx, cy))
        self.mask = pygame.mask.from_surface(self.image)
    
    def move(self):
        self.rect.y -= VELB

        if self.rect.y <= -50:
            self.kill()

class Cacto_invertido(pygame.sprite.Sprite):
    def __init__(self, cx, cy):
        super().__init__()
        self.image = pygame.image.load("./sprites/enemy/cacto_invertido.png")
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (cx, cy))
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.y += VEL 

        if self.rect.y >= 650:
            self.kill()