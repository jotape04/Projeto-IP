import pygame 
from cactos import Cacto, Cacto_invertido
from shooter import Shooter
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

shooter = Shooter()

grupo_cactos = pygame.sprite.Group()
grupo_cactos.add(cacto1, cacto2, cacto3, cacto4, cacto5, minicacto1, minicacto2)

grupo_shooter = pygame.sprite.Group()
grupo_shooter.add(shooter)


#Definindo Função que calcula a distância entre o personagem e os cactos que vão se movimentar
def distancia_cacto_personagem(cacto, personagem):
    distancia =  ((cacto.rect.y - personagem.rect.y)**2 + (cacto.rect.x - personagem.rect.x)**2)**(1/2)
    return distancia

#Definindo função pro movimento dos cactos
def movimento_pra_cima(cacto):
    cacto.rect.y -= 2

def movimento_pra_baixo(cacto):
    cacto.rect.y += 2

#Variáveis booleanas que indicam quando foi a primeira vez que o personagem atingiu a distância
mínima pra cada um dos cactos se movimentar
primeira_interacao1 = True
primeira_interacao2 = True
primeira_interacao3 = True

#Regula o número de frames
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
                shooter.rect.y -= 5

            if event.key == K_LEFT:
                shooter.rect.x -= 5

            if event.key == K_RIGHT:
                shooter.rect.x += 5
            
            if event.key == K_DOWN:
                shooter.rect.y += 5
                
    #Criando o movimento com teclas PRESSIONADAS
    if pygame.key.get_pressed()[K_UP]:
        shooter.rect.y -= 5

    if pygame.key.get_pressed()[K_DOWN]:
        shooter.rect.y += 5

    if pygame.key.get_pressed()[K_LEFT]:
        shooter.rect.x -= 5

    if pygame.key.get_pressed()[K_RIGHT]:
        shooter.rect.x += 5
       
       
    # A distância entre o atirador e cada cacto só é calculada até ele atingir a distância mínima
    para o movimento do cacto
    if primeira_interacao1:
        distancia1 = distancia_cacto_personagem(cacto1, shooter)

    if primeira_interacao2:
       distancia2 =  distancia_cacto_personagem(cacto2, shooter) 

    if primeira_interacao3:
        distancia3 = distancia_cacto_personagem(cacto3, shooter) 

    #Analisa a primeira vez que o atirador se aproxima do CACTO 1
    if distancia1 <= 70 and primeira_interacao1:

        #Impede o progama de calcular a distância a cada loop do jogo
        primeira_interacao1 = False

        #Salva as coordenadas y do cacto e do atirador na primeira vez que eles atingiram a distância mínima pro movimento
        y_shooter = shooter.rect.y
        y_cacto1 = cacto1.rect.y
        
        #56 é a altura do cacto 
        if cacto1.rect.y > -56:
            movimento_pra_cima(cacto1)
    
    if not primeira_interacao1:
        
        #56 é a altura do cacto 
        if cacto1.rect.y > -56:
            movimento_pra_cima(cacto1)
    
    
    #Analisa a primeira vez que o personagem se aproxima do CACTO 2
    if distancia2 <= 85 and primeira_interacao2:

        #Impede o progama de calcular a distância a cada loop do jogo
        primeira_interacao2 = False

        #Salva as coordenadas y do cacto e do atirador na primeira vez que eles atingiram a distância mínima pro movimento
        y_shooter = shooter.rect.y
        y_cacto2 = cacto2.rect.y

       if cacto2.rect.y < 600:
            movimento_pra_baixo(cacto2)

    if not primeira_interacao2:

        if cacto2.rect.y < 600:
            movimento_pra_baixo(cacto2)

    #Analisa a primeira vez que o personagem se aproxima do CACTO 3
    if distancia3 <= 85 and primeira_interacao3 :

       #Impede o progama de calcular a distância a cada loop do jogo
        primeira_interacao3 = False

        #Salva as coordenadas y do cacto e do atirador na primeira vez que eles atingiram a distância mínima pro movimento
        y_shooter = shooter.rect.y
        y_cacto3 = cacto3.rect.y

        if cacto3.rect.y < 600:
            movimento_pra_baixo(cacto3)
            
    if not primeira_interacao3 :

        if cacto3.rect.y < 600:
           movimento_pra_baixo(cacto3)

    grupo_shooter.draw(tela)
    grupo_cactos.draw(tela)
    pygame.display.update()
    tela.blit(background,(0,0))
