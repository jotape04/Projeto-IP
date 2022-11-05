import pygame
from random import randint

class Coletavel():
    def __init__(self, cor):
        self.cor = cor       
        self.obj = pygame.Rect(randint(0, 495), randint(0, 495), 10, 10)
        return
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, self.obj)
        return
    
    def coletou(self):
        self.obj.x = randint(0,495)
        self.obj.y = randint(0,495)    
        