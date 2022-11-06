from random import randint
from tracemalloc import start
import pygame
import movimentacao
from pers import Personagem
from colet import Coletavel

pygame.init()

telax = 500
telay = 500

win = pygame.display.set_mode((telax, telay))

pygame.display.set_caption("retangulo correndo")

# puxando fontes:
fonte = pygame.font.Font('freesansbold.ttf', 32)
fnt_tempo = pygame.font.Font('freesansbold.ttf', 20)

pontuacao1 = 7
pontuacao2 = 5
pontuacao3 = 3

ganhou = False

# item coletavel 1:
hc = 10
wc = 10

# pygame rodando
run = True

quitou = False

objeto = Personagem(20, 3, (255, 0, 0))

coletavel1 = Coletavel((255, 255, 255))
coletavel2 = Coletavel((160, 32, 240))
coletavel3 = Coletavel((0, 0, 255))

# tempo em segundos
start_time = pygame.time.get_ticks()

pygame.mixer.music.load('music/stranger-things-124008.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

# loop infinito
while run:
    # delay de 8ms
    pygame.time.delay(8)

    act_time = pygame.time.get_ticks()
    tempo = 20 - ((act_time - start_time) // 1000)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            quitou = True

            run = False

    if pontuacao1 == 0 and pontuacao2 == 0 and pontuacao3 == 0:
        ganhou = True
        run = False

    if tempo == 0:
        run = False

    movimentacao.mov(objeto, 500, 500, objeto.dim)

    coletou1 = objeto.obj.colliderect(coletavel1.obj)
    coletou2 = objeto.obj.colliderect(coletavel2.obj)
    coletou3 = objeto.obj.colliderect(coletavel3.obj)

    # se tiver coletado:
    gap = 10

    if coletou1:
        if pontuacao1 > 0:
            pontuacao1 -= 1

        coletavel1.coletou()

    if coletou2:
        if pontuacao2 > 0:
            pontuacao2 -= 1

        coletavel2.coletou()

    if coletou3:
        if pontuacao3 > 0:
            pontuacao3 -= 1

        coletavel3.coletou()

    # pintando o background
    win.fill((0, 0, 0))

    # escrevendo na tela:
    # puxando fontes:
    fonte = pygame.font.Font('freesansbold.ttf', 32)
    fnt_tempo = pygame.font.Font('freesansbold.ttf', 20)
    # criando a escrita:
    pont1 = fonte.render(str(pontuacao1), True, (255, 255, 255), (0, 0, 0))
    pont2 = fonte.render(str(pontuacao2), True, (160, 32, 240), (0, 0, 0))
    pont3 = fonte.render(str(pontuacao3), True, (0, 0, 255), (0, 0, 0))

    time_text = fnt_tempo.render("tempo: " + str(tempo), True, (255, 0, 0))

    pos_time = time_text.get_rect()
    pos_time.center = (telax - pos_time.width - 20,
                       telay - pos_time.height - 20)

    win.blit(pont1, (20, 20))
    win.blit(pont2, (245, 20))
    win.blit(pont3, (telax - 30, 20))
    win.blit(time_text, pos_time)

    # desenhando o objeto que se move e o coletavel
    coletavel1.draw(win)

    coletavel2.draw(win)

    coletavel3.draw(win)

    objeto.draw(win)

    # fazendo update na janela
    pygame.display.update()

pygame.mixer.music.stop()

run = True
while run:
    win.fill((0, 0, 0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            run = False

    if ganhou:
        mensagem = "Parabéns, você conseguiu!"
    elif quitou:
        mensagem = "Ficou bravinho?"
    else:
        mensagem = "Tente novamente"

    msg_final = fnt_tempo.render(mensagem, True, (0, 255, 0))
    sup_final = msg_final.get_rect()

    sup_final.center = (telax/2, telay/2)

    win.blit(msg_final, sup_final)

    pygame.display.update()
