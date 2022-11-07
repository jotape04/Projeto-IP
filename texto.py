import pygame

class Death(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "sprites/mapa/morte.png")
        self.rect = self.image.get_rect(center= (600, 300))

class Vic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            "sprites/mapa/victory.png")
        self.rect = self.image.get_rect(center= (600, 300))

class Texto():
# escrevendo na tela:
    def __init__(self):

        self.fonte = pygame.font.Font('freesansbold.ttf', 25)
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0

        # criando a escrita:
        self.texto1 = self.fonte.render("Pexeira: " + str(0),
                          True, (0, 0, 0))
        self.texto2 = self.fonte.render("Calango: " + str(0),
                          True, (0, 0, 0))
        self.texto3 = self.fonte.render("Agua: " + str(0),
                          True, (0, 0, 0))

        # criando a superficie:
        self.escrever1 = self.texto1.get_rect()
        self.escrever2 = self.texto2.get_rect()
        self.escrever3 = self.texto3.get_rect()

        self.escrever1.center = (350, 20)
        self.escrever2.center = (600, 20)
        self.escrever3.center = (850, 20)

    def up1(self):
        self.p1 += 1
        self.texto1 = self.fonte.render("Pexeira: " + str(self.p1),
                          True, (0, 0, 0))
        
    def up2(self):
        self.p2 += 1
        self.texto2 = self.fonte.render("Calango: " + str(self.p2),
                          True, (0, 0, 0))
        
    def up3(self):
         self.p3 += 1
         self.texto3 = self.fonte.render("Agua: " + str(self.p3),
                          True, (0, 0, 0))

    