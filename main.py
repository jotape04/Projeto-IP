from cactos import Cacto, Cacto_invertido
from character import Alagoano
from pygame import mixer
from coletaveis import *
from random import randint
from shooter import Shooter
from texto import *
import pygame
import time

width = 1200
height = 600

def victory():
    mixer.music.load("./music/vic.mp3")
    mixer.music.play()
    
    ganho = Vic()
    vitoria = pygame.sprite.Group()
    vitoria.add(ganho)

    vitoria.draw(win)
    pygame.display.update()

    time.sleep(5)
    return False

def gameover():
    #toca a musica de morte
    mixer.music.load("./music/over.mp3")
    mixer.music.play()
    
    #coloca na tela a mensagem de morte
    death = Death()
    morte = pygame.sprite.Group()
    morte.add(death)

    morte.draw(win)
    pygame.display.update()
    
    #espera 5 segundos e reinicia o jogo
    time.sleep(5)
    return jogo()


#Definindo Função que calcula a distância entre o personagem e os cactos que vão se movimentar
def distancia_cacto_personagem(cacto, personagem):
    distancia =  ((cacto.rect.y - personagem.rect.y)**2 + (cacto.rect.x - personagem.rect.x)**2)**(1/2)
    return distancia

#Definindo função pro movimento dos cactos
def movimento_pra_cima(cacto):
    cacto.rect.y -= 2

def movimento_pra_baixo(cacto):
    cacto.rect.y += 2
   
# colisão do alagoano com as boxes dos cactos
def colisao_box_cactos(personagem):
       if 0 <= personagem.rect.y <= 149 and 0 <= personagem.rect.x <= 51:
            return gameover()
       elif 0 <= personagem.rect.y <= 42 and 57 <= personagem.rect.x <= 178:
            return gameover()

       elif 382 <= personagem.rect.y <= 600 and 0 <= personagem.rect.x <= 48:
            return gameover() 

       elif 477 <= personagem.rect.y <= 600  and 51 <= personagem.rect.x <= 173:
            return gameover()

       elif 335 <= personagem.rect.y <= 393 and 265 <= personagem.rect.x <= 378:
            return gameover()

       elif 335 <= personagem.rect.y <= 375 and 593 <= personagem.rect.x <= 819:
            return gameover()
    
       elif 206 <= personagem.rect.y <= 284 and 373 <= personagem.rect.x <= 791:
            return gameover()

def jogo():
    #comeca a tocar a musica de fundo
    mixer.init()
    musica = mixer.music.load("./music/gameost.mp3")
    mixer.music.set_volume(0.4)
    mixer.music.play(-1)

    texto = Texto()

    # pygame rodando
    run = True

    # pulo
    pulo = 0
    
    #criando coletaveis
    agua = Agua()
    _agua = pygame.sprite.Group()
    _agua.add(agua)
    
    peixeira = Peixeira()
    _peixeira = pygame.sprite.Group()
    _peixeira.add(peixeira)
    
    calango = Calango()
    _calango = pygame.sprite.Group()
    _calango.add(calango)

    # coloca o atirador em campo
    shoot = Shooter()
    shooter = pygame.sprite.Group()
    shooter.add(shoot)

    # alagoano
    alagoano = Alagoano()
    player = pygame.sprite.Group()
    player.add(alagoano)

    #coloca os cactos em campo
    cacto1 = Cacto((27, 50.4), 194, 565 )
    cacto2 = Cacto_invertido(586, 372)
    cacto3 = Cacto_invertido(843, 372)
    cacto4 = Cacto_invertido(880, 378)
    cacto5 = Cacto_invertido(546, 378)
    minicacto1 = Cacto((27*0.2, 50.4*0.2),79, 335)
    minicacto2 = Cacto((27*0.2, 50.4*0.2),739,173)  
    grupo_cactos = pygame.sprite.Group()
    grupo_cactos.add(cacto1, cacto2, cacto3, cacto4, cacto5, minicacto1, minicacto2)

    # coloca as balas
    bullets = pygame.sprite.Group()

    # começa o timer para as balas
    now = time.time()
    tbase = time.time()
    tpulo = time.time()

    # regula a interação do alagoano com os cactos que vão se movimentar
    primeira_interacao1 = True
    primeira_interacao2 = True
    primeira_interacao3 = True

    # número de frames
    relogio = pygame.time.Clock()

    # loop do game
    while run:

        relogio.tick(30)
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
            if event.type == pygame.MOUSEBUTTONUP:
                print(pygame.mouse.get_pos())

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

            if time.time() - tpulo > 0.43:
                pulo = alagoano.down()
                alagoano.base()
            else:
                alagoano.up()
        else:
            pulo = alagoano.down()
            if time.time() - tbase > 0.2:
                alagoano.base()
                
        # movimento dos cactos
        if primeira_interacao1:
           distancia1 = distancia_cacto_personagem(cacto1, alagoano)

        if primeira_interacao2:
           distancia2 =  distancia_cacto_personagem(cacto2, alagoano) 

        if primeira_interacao3:
           distancia3 = distancia_cacto_personagem(cacto3, alagoano)
        
        if distancia1 <= 70 and primeira_interacao1:

            # fixa a distânica do personagem pro cacto
            primeira_interacao1 = False

            # Salva as coordenadas y do cacto e do atirador na primeira vez que eles atingiram a distância mínima pro movimento
            y_alagoano = alagoano.rect.y
            y_cacto1 = cacto1.rect.y

            if cacto1.rect.y > -56:
               movimento_pra_cima(cacto1)

        if not primeira_interacao1:

            if cacto1.rect.y > -56:
               movimento_pra_cima(cacto1)
    
        #Analisa a primeira vez que o personagem se aproxima do CACTO 2
        if distancia2 <= 100 and primeira_interacao2:

             # fixa a distânica do personagem pro cacto
            primeira_interacao2 = False

            # Salva as coordenadas y do cacto e do atirador na primeira vez que eles atingiram a distância mínima pro movimento
            y_alagoano = alagoano.rect.y
            y_cacto2 = cacto2.rect.y

            if cacto2.rect.y < 600:
                movimento_pra_baixo(cacto2)

        if not primeira_interacao2:

            if cacto2.rect.y < 600:
                movimento_pra_baixo(cacto2)

        #Analisa a primeira vez que o personagem se aproxima do CACTO 3
        if distancia3 <= 100 and primeira_interacao3 :

            #Impede o progama de executar linhas de código desnecessárias
            primeira_interacao3 = False

            #Salva as coordenadas y do cacto e do atirador na primeira vez que eles atingiram a distância mínima pro movimento
            y_alagoano = alagoano.rect.y
            y_cacto3 = cacto3.rect.y

            if cacto3.rect.y < 600:
                movimento_pra_baixo(cacto3)

        if not primeira_interacao3 :

            if cacto3.rect.y < 600:
                movimento_pra_baixo(cacto3)
        
        # colisões das sprites
        colisoes1 = pygame.sprite.spritecollide(alagoano, grupo_cactos, False, pygame.sprite.collide_mask)
        if colisoes1:
            gameover()

        colisoes2 = pygame.sprite.spritecollide(alagoano, shooter, False, pygame.sprite.collide_mask )
        if colisoes2:
            gameover()

        colisoes3 = pygame.sprite.spritecollide(alagoano, bullets, False, pygame.sprite.collide_mask)
        if colisoes3:
            gameover()
            
        # colisões com as boxes dos cactos
        colisao_box_cactos(alagoano)
                
        if pygame.sprite.spritecollide(alagoano, _peixeira, True):
            texto.up1
        elif pygame.sprite.spritecollide(alagoano, _calango, True):
            texto.up2
        elif pygame.sprite.spritecollide(alagoano, _agua, True):
            texto.up3
            
        # desenhado o alagoan
        player.draw(win)

        # desenhando o atirador
        bullets.draw(win)
        shooter.draw(win)

        # desenhando os cactos
        grupo_cactos.draw(win)

        # movimentação das balas
        bullets.update(width)
        
        #escreve a contagem dos coletáveis
        win.blit(texto.texto1, texto.escrever1)
        win.blit(texto.texto2, texto.escrever2)
        win.blit(texto.texto3, texto.escrever3)

        pygame.display.flip()

        #checa se o jogador ganhou
        if texto.p1 == texto.p2 == texto.p3 == 1:
            return victory()

        
pygame.init()
win = pygame.display.set_mode((width, height))

bg_img = pygame.image.load('./sprites/mapa/mapateste2.png')
bg_img = pygame.transform.scale(bg_img, (width, height))

pygame.display.set_caption("Alagoaninho Adventures")

jogar = True
while jogar:
    jogar = jogo()
