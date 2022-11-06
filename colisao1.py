import pygame
from alagoano import Alagoano 
from cactos import Cacto, Cacto_invertido
from pygame.locals import *


pygame.init()

largura = 1200
altura = 600
tela = pygame.display.set_mode((largura, altura))

background = pygame.image.load('sprites/mapateste2.png')
background = pygame.transform.scale(background,(largura, altura))

#Colocando os objetos em um grupo
cacto1 = Cacto((27, 50.4), 194, 565 )
cacto2 = Cacto_invertido(586, 372)
cacto3 = Cacto_invertido(843, 372)
cacto4 = Cacto_invertido(880, 378)
cacto5 = Cacto_invertido(546, 378)
minicacto1 = Cacto((27*0.2, 50.4*0.2),79, 335)
minicacto2 = Cacto((27*0.2, 50.4*0.2),739,173)

alagoano = Alagoano()

grupo_cactos = pygame.sprite.Group()
grupo_cactos.add(cacto1, cacto2, cacto3, cacto4, cacto5, minicacto1, minicacto2)

grupo_shooter = pygame.sprite.Group()
grupo_shooter.add(alagoano)

#Regula os frames
relogio = pygame.time.Clock()

#Loop do jogo
while True :
    relogio.tick(30)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            exit()

        #Movimento do Personagem
        if event.type == KEYDOWN:

            if event.key == K_UP:
                alagoano.rect.y -= 5

            if event.key == K_LEFT:
                alagoano.rect.x -= 5

            if event.key == K_RIGHT:
                alagoano.rect.x += 5
            
            if event.key == K_DOWN:
               alagoano.rect.y += 5

    if pygame.key.get_pressed()[K_UP]:
        alagoano.rect.y -= 5

    if pygame.key.get_pressed()[K_DOWN]:
        alagoano.rect.y += 5

    if pygame.key.get_pressed()[K_LEFT]:
        alagoano.rect.x -= 5

    if pygame.key.get_pressed()[K_RIGHT]:
        alagoano.rect.x += 5

    grupo_shooter.draw(tela)
    grupo_cactos.draw(tela)

    #Colisões com os retângulos dos cactos
    if 0 <= alagoano.rect.y <= 149 and 0 <= alagoano.rect.x <= 51:
        print('colidiu')

    elif 0 <= alagoano.rect.y <= 42 and 57 <= alagoano.rect.x <= 178:
        print('colidiu')

    elif 382 <= alagoano.rect.y <= 600 and 0 <= alagoano.rect.x <= 48:
        print('colidiu')

    elif 477 <= alagoano.rect.y <= 600  and 51 <= alagoano.rect.x <= 173:
        print('colidiu')

    elif 335 <= alagoano.rect.y <= 393 and 265 <= alagoano.rect.x <= 378:
        print('colidiu')

    elif 335 <= alagoano.rect.y <= 387 and 593 <= alagoano.rect.x <= 819:
        print('colidiu')
    
    elif 206 <= alagoano.rect.y <= 284 and 373 <= alagoano.rect.x <= 791:
        print('colidiu')

    else:
        pygame.display.flip()

        
    tela.blit(background,(0,0))