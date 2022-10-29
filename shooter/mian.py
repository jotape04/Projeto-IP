from random import randint
from shooter import Shooter
import pygame
import time

pygame.init()

height = 600
width = 1200

win = pygame.display.set_mode((width, height))

bg_img = pygame.image.load('./sprites/mapa/mapateste2.png')
bg_img = pygame.transform.scale(bg_img, (width, height))

pygame.display.set_caption("Alagoaninho Adventures")

pontuacao1 = 0
pontuacao2 = 0
pontuacao3 = 0

# posicao do objeto
x = 1110
y = 520

altura_colataveis = 15
largura_coletaveis = 15

# item coletavel 1:
cx1 = randint(0, 1100)
cy1 = randint(0, 500)

# item coletavel 2:
cx2 = randint(0, 1100)
cy2 = randint(0, 500)

# item coletavel 3:
cx3 = randint(0, 1100)
cy3 = randint(0, 500)

# dimensionando o objeto
width = 20
height = 20

# velocidade do bloco
vel = 5

# pygame rodando
run = True


objeto = pygame.Rect(x, y, width, height)

coletavel1 = pygame.Rect(cx1, cy1, largura_coletaveis, altura_colataveis)

coletavel2 = pygame.Rect(cx2, cy2, largura_coletaveis, altura_colataveis)

coletavel3 = pygame.Rect(cx3, cy3, largura_coletaveis, altura_colataveis)

#coloca o atirador em campo
shoot = Shooter()
shooter = pygame.sprite.Group()
shooter.add(shoot)

#coloca as balas
bullets = pygame.sprite.Group()

#começa o timer para as balas
now = time.time()
# loop do game
while run:
    # aplica o background
    win.blit(bg_img, (0, 0))

    # cria delay de 10s
    pygame.time.delay(10)

    # iterando os eventos do pygame
    for event in pygame.event.get():

        # se o evento for do tipo QUIT
        if event.type == pygame.QUIT:

            # saindo do loop
            run = False

    keys = pygame.key.get_pressed()

    #atirador voltando a posição base
    if 1.1 > time.time() - now > 0.9:
        shoot.wait()
    #se preparando pra atirar
    if 1.8 > time.time() - now > 1.6:
        shoot.prepare()
    #atirando a bala
    if 2.1 > time.time() - now > 1.9:
        now = time.time()
        bullets.add(shoot.createb())
    

    # se a seta para esquerda for pressionada
    if keys[pygame.K_LEFT] and objeto.x > 0:

        # diminuindo no eixo x
        objeto.x -= vel

    # se a seta para a direita for pressionada
    if keys[pygame.K_RIGHT] and objeto.x < 1200-width:

        # incrementando no eixo x
        objeto.x += vel

    # se a seta para cima for pressionada
    if keys[pygame.K_UP] and objeto.y > 0:

        # diminuindo no eixo y
        objeto.y -= vel

    # se a seta para baixo for pressionada
    if keys[pygame.K_DOWN] and objeto.y < 600-height:
        # incrementando no eixo y
        objeto.y += vel

    coletou1 = objeto.colliderect(coletavel1)
    coletou2 = objeto.colliderect(coletavel2)
    coletou3 = objeto.colliderect(coletavel3)

    # se tiver coletado o coletavel 1:
    if coletou1:
        coletavel1.x = randint(0, 1100)
        coletavel1.y = randint(0, 500)
        pontuacao1 += 1

    # se tiver coletado o coletavel 2:
    if coletou2:
        coletavel2.x = randint(0, 1100)
        coletavel2.y = randint(0, 500)
        pontuacao2 += 1

    # se tiver coletado o coletavel 3:
    if coletou3:
        coletavel3.x = randint(0, 1100)
        coletavel3.y = randint(0, 500)
        pontuacao3 += 1

    # escrevendo na tela:
    # puxando fontes:
    fonte = pygame.font.Font('freesansbold.ttf', 25)

    # criando a escrita:
    texto1 = fonte.render("Branco: " + str(pontuacao1),
                          True, (0, 0, 0))
    texto2 = fonte.render("Rosa: " + str(pontuacao2),
                          True, (0, 0, 0))
    texto3 = fonte.render("Marrom: " + str(pontuacao3),
                          True, (0, 0, 0))

    # criando a superficie:
    escrever1 = texto1.get_rect()
    escrever2 = texto2.get_rect()
    escrever3 = texto3.get_rect()

    escrever1.center = (350, 20)
    win.blit(texto1, escrever1)

    escrever2.center = (600, 20)
    win.blit(texto2, escrever2)

    escrever3.center = (850, 20)
    win.blit(texto3, escrever3)

    #desenhando o atirador
    shooter.draw(win)
    bullets.draw(win)
    #movimentação das balas
    bullets.update(width)
    # desenhando o objeto que se move e o coletavel1
    pygame.draw.rect(win, (255, 255, 255), coletavel1)
    pygame.draw.rect(win, (255, 192, 203), coletavel2)
    pygame.draw.rect(win, (139, 69, 19), coletavel3)

    pygame.draw.rect(win, (255, 0, 0), objeto)

    # fazendo update na janela
    pygame.display.update()
