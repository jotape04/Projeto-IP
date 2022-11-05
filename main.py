from random import randint
from shooter import Shooter
import pygame
import time
from character import Alagoano

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


# pygame rodando
run = True

#pulo
pulo = 0

#coloca o atirador em campo
shoot = Shooter()
shooter = pygame.sprite.Group()
shooter.add(shoot)

#alagonao
alagoano = Alagoano()
player = pygame.sprite.Group()
player.add(alagoano)

#coloca as balas
bullets = pygame.sprite.Group()


#começa o timer para as balas
now = time.time()
tbase = time.time()
tpulo = time.time()
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

        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
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
    if keys[pygame.K_LEFT]:
        tbase = time.time()
        # diminuindo no eixo x
        alagoano.left()

    # se a seta para a direita for pressionada
    if keys[pygame.K_RIGHT]:
        tbase = time.time()
        # incrementando no eixo x
        alagoano.right()

    # se a seta para cima for pressionada
    if keys[pygame.K_UP] and alagoano.lock == 0:

        # diminuindo no eixo y
        alagoano.up()
        tpulo = time.time()
        pulo = 1

    
    #retornando o Alagoano até a posição base
    if pulo == 0:
        if time.time() - tbase > 0.2:
            alagoano.base()
    else:
        alagoano.updatejump()

        if time.time() - tpulo < 0.4:
            alagoano.up()
        else:
            pulo = alagoano.down()
            

        

    #desenhado o alagoan
    player.draw(win)

    #desenhando o atirador
    bullets.draw(win)
    shooter.draw(win)

    #movimentação das balas
    bullets.update(width)
    # fazendo update na janela
    pygame.display.update()

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
