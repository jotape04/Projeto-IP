import time

import pygame
from pygame import mixer

from cactos import *
from character import Alagoano
from coletaveis import *
from shooter import Shooter
from texto import *

pygame.init()

height = 600
width = 1200

win = pygame.display.set_mode((width, height))

bg_img = pygame.image.load('./sprites/mapa/mapateste2.png')
bg_img = pygame.transform.scale(bg_img, (width, height))

pygame.display.set_caption("Alagoaninho Adventures")


def colisao_box_cactos(personagem):
    if 0 <= personagem.rect.y <= 149 and 0 <= personagem.rect.x <= 51:
        return True

    elif 0 <= personagem.rect.y <= 42 and 57 <= personagem.rect.x <= 178:
        return True

    elif 382 <= personagem.rect.y <= 600 and 0 <= personagem.rect.x <= 48:
        return True

    elif 477 <= personagem.rect.y <= 600 and 51 <= personagem.rect.x <= 173:
        return True

    elif 335 <= personagem.rect.y <= 393 and 265 <= personagem.rect.x <= 378:
        return True

    elif 335 <= personagem.rect.y <= 375 and 593 <= personagem.rect.x <= 819:
        return True

    elif 206 <= personagem.rect.y <= 284 and 373 <= personagem.rect.x <= 791:
        return True
    else:
        False


def victory():
    mixer.music.load("./music/vic.mp3")
    mixer.music.play()

    ganho = Vic()
    vitoria = pygame.sprite.Group()
    vitoria.add(ganho)

    vitoria.draw(win)
    pygame.display.update()

    time.sleep(3)
    return False


def gameover():

    mixer.music.load("./music/over.mp3")
    mixer.music.play()

    death = Death()
    morte = pygame.sprite.Group()
    morte.add(death)

    morte.draw(win)
    pygame.display.update()

    time.sleep(2)
    return jogo()


def jogo():
    mixer.init()
    mixer.music.load("./music/gameost.mp3")
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)

    texto = Texto()

    # pygame rodando
    run = True

    # pulo
    pulo = 0

    # coloca o atirador em campo
    shoot = Shooter()
    shooter = pygame.sprite.Group()
    shooter.add(shoot)

    # alagonao
    alagoano = Alagoano()
    player = pygame.sprite.Group()
    player.add(alagoano)

    # coloca os coletaveis
    agua = Agua()
    _agua = pygame.sprite.Group()
    _agua.add(agua)

    calango = Calango()
    _calango = pygame.sprite.Group()
    _calango.add(calango)

    peixeira = Peixeira()
    _peixeira = pygame.sprite.Group()
    _peixeira.add(peixeira)

    # coloca os cactos em campo
    cacto1 = Cacto((27, 50.4), 194, 565)
    cacto2 = Cacto_invertido(586, 372)
    cacto3 = Cacto_invertido(843, 372)
    cacto4 = Cacto_invertido(880, 378)
    cacto5 = Cacto_invertido(546, 378)
    minicacto1 = Cacto((27*0.2, 50.4*0.2), 79, 340)
    minicacto2 = Cacto((27*0.2, 50.4*0.2), 739, 173)
    minicacto3 = Cacto((27*0.2, 50.4*0.2), 730, 173)
    grupo_cactos = pygame.sprite.Group()
    grupo_cactos.add(cacto1, cacto2, cacto3, cacto4, cacto5,
                     minicacto1, minicacto2, minicacto3)

    #
    c1 = 0
    c2 = 0
    c3 = 0

    # coloca as balas
    bullets = pygame.sprite.Group()

    # se houve colisão com cacto
    colc = False

    # começa o timer para as balas
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
                return False

        keys = pygame.key.get_pressed()

        # atirador voltando a posição base
        if 1.1 > time.time() - now > 0.9:
            shoot.wait()
        # se preparando pra atirar
        if 1.8 > time.time() - now > 1.6:
            shoot.prepare()
        # atirando a bala
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

        # retornando o Alagoano até a posição base
        if pulo == 1:
            alagoano.updatejump()

            if time.time() - tpulo > 0.35:
                pulo = alagoano.down()
                alagoano.base()
            else:
                alagoano.up()
        else:
            pulo = alagoano.down()
            if time.time() - tbase > 0.2:
                alagoano.base()

        if pygame.sprite.spritecollide(alagoano, _peixeira, True):
            texto.up1()

        if pygame.sprite.spritecollide(alagoano, _calango, True):
            texto.up2()

        if pygame.sprite.spritecollide(alagoano, _agua, True):
            texto.up3()

        # desenhado o alagoan
        player.draw(win)

        # desenhando o atirador
        bullets.draw(win)
        shooter.draw(win)

        # desenhando os cactos
        grupo_cactos.draw(win)

        # desenhando os coletaveis
        _peixeira.draw(win)
        _agua.draw(win)
        _calango.draw(win)

        # movimentação das balas
        bullets.update()

        win.blit(texto.texto1, texto.escrever1)
        win.blit(texto.texto2, texto.escrever2)
        win.blit(texto.texto3, texto.escrever3)

        # fazendo update na janela
        pygame.display.update()
        if 205 <= alagoano.rect.x <= 230:
            c1 = 1

        if 820 <= alagoano.rect.x <= 857:
            c3 = 1

        if 558 <= alagoano.rect.x <= 602:
            c2 = 1

        if c1 == 1:
            cacto1.move()
        if c3 == 1:
            cacto3.move()
        if c2 == 1:
            cacto2.move()

        if pygame.sprite.spritecollide(alagoano, grupo_cactos, True):
            return gameover()

        if pygame.sprite.spritecollide(alagoano, shooter, True):
            return gameover()

        if pygame.sprite.spritecollide(alagoano, bullets, True):
            return gameover()

        colc = colisao_box_cactos(alagoano)
        if colc:
            return gameover()

        if texto.p1 == texto.p2 == texto.p3 == 1:
            return victory()


jogar = True
while jogar:
    jogar = jogo()
