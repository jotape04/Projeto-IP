import pygame


VEL = 5
ATT = 7


class Alagoano(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "sprites/alagoaninho/alagoaninho-parado.png")
        self.rect = self.image.get_rect(center=(1116, 526))
        self.direction = 1  # 1 é direita 0 é esquerda
        self.walk = 0
        self.jumpi = 0
        self.lock = 0

    def base(self):
        if self.direction == 0:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-parado(IN).png")
        elif self.direction == 1:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-parado.png")

    def right(self):
        self.direction = 0
        if 250 < self.rect.x < 300  and 203 < self.rect.y < 365:
            pass
        elif 843 < self.rect.x < 867  and 203 < self.rect.y < 365:
            pass
        elif (self.rect.x < 1120):
            self.rect.x += VEL

        if self.walk < ATT and self.jumpi == 0:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-andando(IN).png")
            self.walk += 1
        elif self.walk == ATT and self.jumpi == 0:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-parado(IN).png")
            self.walk += 1
        elif self.walk == 8 and self.jumpi == 0:
            self.walk = 0

    def left(self):
        self.direction = 1
        if 270 < self.rect.x < 310  and 203 < self.rect.y < 365:
            pass
        elif 873 < self.rect.x < 897  and 203 < self.rect.y < 365:
            pass
        elif (self.rect.x > 20):
            self.rect.x -= VEL

        if self.walk < ATT and self.jumpi == 0:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-andando.png")
            self.walk += 1
        elif self.walk == ATT and self.jumpi == 0:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-parado.png")
            self.walk += 1
        elif self.walk == 8 and self.jumpi == 0:
            self.walk = 0

    def down(self):
        if (855 > self.rect.x > 300 and 300 > self.rect.y > 290):
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 1050 > self.rect.x > 765 and 430 < self.rect.y < 440:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 610 > self.rect.x > 480 and 430 < self.rect.y < 440:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 125 > self.rect.x > 45 and 425 < self.rect.y < 435:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 235 > self.rect.x > 155 and 340 < self.rect.y < 350:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 95 > self.rect.x > 25 and 290 < self.rect.y < 300:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 205 > self.rect.x > 125 and 220 < self.rect.y < 230:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 115 > self.rect.x > 35 and 130 < self.rect.y < 140:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 305 > self.rect.x > 265 and 160 < self.rect.y < 170:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 480 > self.rect.x > 405 and 130 < self.rect.y < 140:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 890 > self.rect.x > 825 and 160 < self.rect.y < 180:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 1070 > self.rect.x > 1000 and 130 < self.rect.y < 140:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif 755 > self.rect.x > 675 and 130 < self.rect.y < 140:
            self.jumpi = 0
            self.lock = 0
            return 0
        elif self.rect.y < 504:
            self.rect.y += VEL * 1.75
            return 1
        else:
            self.jumpi = 0
            self.lock = 0
            return 0

    def up(self):
        self.lock = 1
        self.jumpi = 1
        if (570 > self.rect.x > 380 and 360 > self.rect.y > 300) or (895 > self.rect.x > 810 and 360 > self.rect.y > 300):
            pass
        elif self.rect.y > -5:
            self.rect.y -= VEL * 1.26

        if self.direction == 0:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-pulando(IN).png")
        elif self.direction == 1:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-pulando.png")

    def updatejump(self):
        if self.direction == 0:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-pulando(IN).png")
        elif self.direction == 1:
            self.image = pygame.image.load(
                "sprites/alagoaninho/alagoaninho-pulando.png")
