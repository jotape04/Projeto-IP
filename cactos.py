from cmath import rect
import pygame

pygame.init()

#Classes dos cactos que se movem no jogo
class Cacto1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/cacto.png")
        self.image = pygame.transform.scale(self.image, (15*1.8, 28*1.8))
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(bottomleft = (194, 565))

class Cacto2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/cacto_invertido.png")
        self.image = pygame.transform.scale(self.image, (15*1.8, 28*1.8))
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (586, 364))

class Cacto3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/cacto_invertido.png")
        self.image = pygame.transform.scale(self.image, (15*1.8, 28*1.8))
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (843, 362))