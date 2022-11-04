import pygame

def mov(objeto, vel, telax, telay, dim):
    # stores keys pressed 
        keys = pygame.key.get_pressed()
        
        # if left arrow key is pressed
        if keys[pygame.K_LEFT] and objeto.x>0:
            
            # decrement in x co-ordinate
            objeto.x -= vel
            
        # if left arrow key is pressed
        if keys[pygame.K_RIGHT] and objeto.x<telax-dim:
            
            # increment in x co-ordinate
            objeto.x += vel
            
        # if left arrow key is pressed   
        if keys[pygame.K_UP] and objeto.y>0:
            
            # decrement in y co-ordinate
            objeto.y -= vel
            
        # if left arrow key is pressed   
        if keys[pygame.K_DOWN] and objeto.y<telay-dim:
            # increment in y co-ordinate
            objeto.y += vel