from random import randint
from tracemalloc import start
import pygame
import movimentacao

pygame.init()

telax = 500
telay = 500

win = pygame.display.set_mode((telax, telay))

pygame.display.set_caption("retangulo correndo")

#puxando fontes:
fonte = pygame.font.Font('freesansbold.ttf', 32)
fnt_tempo = pygame.font.Font('freesansbold.ttf', 20)
    
pontuacao1 = 7
pontuacao2 = 5
pontuacao3 = 3

ganhou = False
#posicao do objeto
x = 200
y = 200

#item coletavel 1:
hc = 10
wc = 10

c1x = randint(0, telax - wc)
c1y = randint(0, telay - hc)

c2x = randint(0, telax - wc)
c2y = randint(0, telay - hc)

c3x = randint(0, telax - wc)
c3y = randint(0, telay - hc)

  
# dimensions of the object 
width = 20
height = 20
  
# velocidade do bloco
vel = 3.5
  
# pygame rodando
run = True

quitou = False
  
  
objeto = pygame.Rect(x, y, width, height)

coletavel1 = pygame.Rect(c1x, c1y, wc, hc)
coletavel2 = pygame.Rect(c2x, c2y, wc, hc)
coletavel3 = pygame.Rect(c3x, c3y, wc, hc)

#tempo em segundos
start_time = pygame.time.get_ticks()

# loop infinito 
while run:
    # creates time delay of 8ms 
    pygame.time.delay(8)
    
    act_time = pygame.time.get_ticks()
    tempo = 20 - ((act_time - start_time) // 1000)
    
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
            
            quitou = True
            # it will make exit the while loop 
            run = False
    
    if pontuacao1 == 0 and pontuacao2 == 0 and pontuacao3 == 0:
        ganhou = True
        run = False
        
    if tempo == 0:
        run = False
        
        
    movimentacao.mov(objeto, vel, 500, 500, width)
        
    coletou1 = objeto.colliderect(coletavel1)
    coletou2 = objeto.colliderect(coletavel2)
    coletou3 = objeto.colliderect(coletavel3)
    
    #se tiver coletado:
    gap = 10
    
    if coletou1:
        if pontuacao1 > 0:
            pontuacao1 -= 1
        else:
            objeto.x = telax/2
            objeto.y = telay/2
        
        coletavel1.x = randint(0, telax - wc)
        coletavel1.y = randint(0, telax - wc)
        
    
    if coletou2:
        coletavel2.x = randint(0, telax - wc)
        coletavel2.y = randint(0, telay - hc)
        
        if pontuacao2 > 0:
            pontuacao2 -= 1
        else:
            objeto.x = telax/2
            objeto.y = telay/2

    if coletou3:
        if pontuacao3 > 0:
            pontuacao3 -= 1
        else:
            objeto.x = telax/2
            objeto.y = telay/2
        
        coletavel3.x = randint(0, telax - wc)
        coletavel3.y = randint(0, telax - wc)
        
    
         
              
    # pintando o background  
    win.fill((0, 0, 0))
    
    #escrevendo na tela:
    #puxando fontes:
    fonte = pygame.font.Font('freesansbold.ttf', 32)
    fnt_tempo = pygame.font.Font('freesansbold.ttf', 20)
    #criando a escrita:
    pont1 = fonte.render(str(pontuacao1), True, (255,255,255), (0, 0, 0))
    pont2 = fonte.render(str(pontuacao2), True, (160,32,240), (0, 0, 0))
    pont3 = fonte.render(str(pontuacao3), True, (0,0,255), (0, 0, 0))
    
    time_text = fnt_tempo.render("tempo: " + str(tempo), True, (255,0,0))
    
    pos_time = time_text.get_rect()
    pos_time.center = (telax - pos_time.width - 20, telay - pos_time.height - 20)
    
    win.blit(pont1, (20, 20))   
    win.blit(pont2, (245, 20))
    win.blit(pont3, (telax - 30, 20))
    win.blit(time_text, pos_time)
      
    # desenhando o objeto que se move e o coletavel
    pygame.draw.rect(win, (255, 255, 255), coletavel1)
    
    pygame.draw.rect(win, (160,32,240), coletavel2)
    
    pygame.draw.rect(win, (0,0,255), coletavel3)
     
    pygame.draw.rect(win, (255, 0, 0), objeto)
    
    # fazendo update na janela
    pygame.display.update() 
   
run = True 
while run:
    win.fill((0,0,0))   
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    if ganhou:
        mensagem = "Parabéns, você conseguiu!"
    elif quitou:
        mensagem = "Ficou bravinho?"
    else:
        mensagem = "Tente novamente"
        
    msg_final = fnt_tempo.render(mensagem, True, (0,255,0))
    sup_final = msg_final.get_rect()
    
    sup_final.center = (telax/2 , telay/2)
    
    win.blit(msg_final, sup_final)
        
    pygame.display.update()