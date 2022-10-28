from random import randint
import pygame

pygame.init()

height = 600
width = 1200

win = pygame.display.set_mode((width, height))

bg_img = pygame.image.load('./sprites/mapa/mapateste2.png')
bg_img = pygame.transform.scale(bg_img, (width, height))

pygame.display.set_caption("Alagoaninho Adventures")

pontuacao = 0

# puxando fontes:
fonte = pygame.font.Font('freesansbold.ttf', 20)

# criando a escrita:
texto = fonte.render("pontuacao: " + str(pontuacao),
                     True, (255, 255, 255), (0, 0, 0))

# criando a superficie:
superficie_escrever = texto.get_rect()

superficie_escrever.center = (250, 20)

# posicao do objeto
x = 1110
y = 520

# item coletavel 1:
cx = randint(0, 500)
cy = randint(0, 500)

hc = 10
wc = 10

# dimensions of the object
width = 20
height = 20

# velocidade do bloco
vel = 3.5

# pygame rodando
run = True


objeto = pygame.Rect(x, y, width, height)

coletavel = pygame.Rect(cx, cy, wc, hc)

# loop infinito
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

    if pontuacao == 10:
        run = False

    keys = pygame.key.get_pressed()

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

    coletou = objeto.colliderect(coletavel)

    # se tiver coletado:
    if coletou:
        coletavel.x = randint(0, 500)
        coletavel.y = randint(0, 500)
        pontuacao += 1

    # escrevendo na tela:
    # puxando fontes:
    fonte = pygame.font.Font('freesansbold.ttf', 32)

    # criando a escrita:
    texto = fonte.render("pontuacao: " + str(pontuacao),
                         True, (255, 255, 255), (0, 0, 0))

    # criando a superficie:
    superficie_escrever = texto.get_rect()

    superficie_escrever.center = (250, 20)
    win.blit(texto, superficie_escrever)

    # desenhando o objeto que se move e o coletavel
    pygame.draw.rect(win, (255, 255, 255), coletavel)

    pygame.draw.rect(win, (255, 0, 0), objeto)

    # fazendo update na janela
    pygame.display.update()
