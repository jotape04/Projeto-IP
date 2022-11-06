import pygame 
from cactos import Cacto, Cacto_invertido
from alagoano import Alagoano
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

#Função Game Over
def _mensagem_(msg, tamanho, cor):
    fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem, True, cor)
    return texto_formatado

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
                alagoano.rect.y -= 20

            if event.key == K_LEFT:
                alagoano.rect.x -= 20

            if event.key == K_RIGHT:
                alagoano.rect.x += 20
            
            if event.key == K_DOWN:
               alagoano.rect.y += 20

    if pygame.key.get_pressed()[K_UP]:
        alagoano.rect.y -= 5

    if pygame.key.get_pressed()[K_DOWN]:
        alagoano.rect.y += 5

    if pygame.key.get_pressed()[K_LEFT]:
        alagoano.rect.x -= 5

    if pygame.key.get_pressed()[K_RIGHT]:
        alagoano.rect.x += 5
       
    #Colocando a lista de colisões
    colisoes = pygame.sprite.spritecollide(alagoano, grupo_cactos, True)
    grupo_shooter.draw(tela)
    grupo_cactos.draw(tela)



    pygame.display.flip() 
    tela.blit(background,(0,0))

        
