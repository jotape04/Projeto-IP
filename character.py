from re import A
import pygame


VEL = 5
ATT = 7


class Alagoano(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-parado.png")
        self.rect = self.image.get_rect(center = (1116, 526))
        self.keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        self.direction = 1 # 1 é direita 0 é esquerda
        self.walk = 0
        self.jumpi = 0
        self.lock = 0

    def base(self):
        if self.direction == 0:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-parado(IN).png")
        elif self.direction == 1:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-parado.png")

    def right(self):
        self.direction = 0
        if self.rect.x < 1120:
            self.rect.x += VEL

        if self.walk < ATT and self.jumpi == 0:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-andando(IN).png")
            self.walk += 1
        elif self.walk == ATT and self.jumpi == 0:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-parado(IN).png")
            self.walk += 1
        elif self.walk == 8 and self.jumpi == 0: 
            self.walk = 0
    
    def left(self):
        self.direction = 1
        if self.rect.x > 20:
            self.rect.x -= VEL

        if self.walk < ATT and self.jumpi == 0:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-andando.png")
            self.walk += 1
        elif self.walk == ATT and self.jumpi == 0:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-parado.png")
            self.walk += 1
        elif self.walk == 8 and self.jumpi == 0: 
            self.walk = 0
        
    def down(self):
        self.base()
        if self.rect.y < 504:
            self.rect.y += VEL * 1.6
            return 1
        else:
            self.jumpi = 0
            self.lock = 0
            return 0
    
    def up(self):
        self.lock = 1
        self.jumpi = 1
        if self.rect.y > -5:
            self.rect.y -= VEL* 1.35

        if self.direction == 0:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-pulando(IN).png")
        elif self.direction == 1:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-pulando.png")
    
    def updatejump(self):
        if self.direction == 0:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-pulando(IN).png")
        elif self.direction == 1:
            self.image = pygame.image.load("sprites/alagoaninho/alagoaninho-pulando.png")