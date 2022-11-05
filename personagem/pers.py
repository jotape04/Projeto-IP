import pygame

class Personagem():
    
    def __init__(self, dim, vel, cor):
        
        self.dim = dim
        self.vel = vel
        self.cor = cor
        
        self.obj = pygame.Rect(250, 250, dim, dim)
        return

    def draw(self, screen):
        pygame.draw.rect(screen, self.cor, self.obj)
        return
    
    def left_arrow(self):
        self.obj.x -= self.vel
        return
    
    def right_arrow(self):
        self.obj.x += self.vel
        return
      
    def up_arrow(self):
        self.obj.y -= self.vel
        return
    
    def down_arrow(self):
        self.obj.y += self.vel
        return
        
objeto = Personagem(5,5,(0,0,0))

print(objeto.__dict__)