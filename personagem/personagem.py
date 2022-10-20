from random import randint
import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("retangulo correndo")

pontuacao = 0

#puxando fontes:
fonte = pygame.font.Font('freesansbold.ttf', 20)

#criando a escrita:
texto = fonte.render("pontuacao: " + str(pontuacao), True, (255,255,255), (0, 0, 0))

#criando a superficie:
superficie_escrever = texto.get_rect()

superficie_escrever.center = (250, 20)

#posicao do objeto
x = 200
y = 200

#item coletavel 1:
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
    # creates time delay of 10ms 
    pygame.time.delay(10)
    
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    
    if pontuacao == 10:
        run = False
        
    # stores keys pressed 
    keys = pygame.key.get_pressed()
      
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and objeto.x>0:
          
        # decrement in x co-ordinate
        objeto.x -= vel
          
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and objeto.x<500-width:
          
        # increment in x co-ordinate
        objeto.x += vel
         
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and objeto.y>0:
          
        # decrement in y co-ordinate
        objeto.y -= vel
          
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and objeto.y<500-height:
        # increment in y co-ordinate
        objeto.y += vel
        
    coletou = objeto.colliderect(coletavel)
    
    #se tiver coletado:
    if coletou:
        print("coletou")
        coletavel.x = randint(0, 500)
        coletavel.y = randint(0, 500)
        pontuacao += 1
         
              
    # pintando o background  
    win.fill((0, 0, 0))
    
    #escrevendo na tela:
    #puxando fontes:
    fonte = pygame.font.Font('freesansbold.ttf', 32)

    #criando a escrita:
    texto = fonte.render("pontuacao: " + str(pontuacao), True, (255,255,255), (0, 0, 0))

    #criando a superficie:
    superficie_escrever = texto.get_rect()

    superficie_escrever.center = (250, 20)
    win.blit(texto, superficie_escrever)   
      
    # desenhando o objeto que se move e o coletavel
    pygame.draw.rect(win, (255, 255, 255), coletavel)
    
    pygame.draw.rect(win, (255, 0, 0), objeto)
    
    
      
    # fazendo update na janela
    pygame.display.update() 
