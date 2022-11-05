import pygame
from pers import Personagem

def mov(objeto, telax, telay, dim):
    # eventos de setas pressionadas 
        keys = pygame.key.get_pressed()
        
        # seta esquerda
        if keys[pygame.K_LEFT] and objeto.obj.x>0:
            
            objeto.left_arrow()
        
        # seta direita
        if keys[pygame.K_RIGHT] and objeto.obj.x<telax-dim:
            
            objeto.right_arrow()
            
        # seta para cima  
        if keys[pygame.K_UP] and objeto.obj.y>0:
            
            objeto.up_arrow()
            
        # seta para baixo   
        if keys[pygame.K_DOWN] and objeto.obj.y<telay-dim:
            
            objeto.down_arrow()