import pygame

class Texto():
# escrevendo na tela:
    def __init__(self, p1, p2, p3):

        self.fonte = pygame.font.Font('freesansbold.ttf', 25)

    # criando a escrita:
        self.texto1 = self.fonte.render("Branco: " + str(p1),
                          True, (0, 0, 0))
        self.texto2 = self.fonte.render("Rosa: " + str(p2),
                          True, (0, 0, 0))
        self.texto3 = self.fonte.render("Marrom: " + str(p3),
                          True, (0, 0, 0))

        # criando a superficie:
        self.escrever1 = self.texto1.get_rect()
        self.escrever2 = self.texto2.get_rect()
        self.escrever3 = self.texto3.get_rect()

        self.escrever1.center = (350, 20)
        self.escrever2.center = (600, 20)
        self.escrever3.center = (850, 20)

    