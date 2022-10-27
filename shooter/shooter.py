from turtle import width, ycor
import pygame, sys

class Shooter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/enemy/cangaciro2.png")
        #self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center = (200, 200))

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def createb(self):
        return Bullets(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    
    def prepare(self):
        self.image = pygame.image.load("sprites/enemy/cangaciro1.png")

    def wait(self):
        self.image = pygame.image.load("sprites/enemy/cangaciro2.png")

class Bullets(pygame.sprite.Sprite):
    def __init__(self, px, py):
        super().__init__()
        self.image = pygame.image.load("sprites/enemy/bullet.png")
        self.rect = self.image.get_rect(center = (px + 20, py - 22))

    def update(self, xx):
        self.rect.x += 15

        if self.rect.x > xx + 200:
            self.kill
        