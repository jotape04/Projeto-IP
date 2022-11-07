import pygame

class Agua(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./sprites/coletaveis/agua.png")
        
        self.image = pygame.transform.scale(self.image, (30, 30)) 
        
        self.rect = self.image.get_rect()
        
        self.rect.center = (1056, 155)
    
    
class Peixeira(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./sprites/coletaveis/peixeira.png")
        
        self.image = pygame.transform.scale(self.image, (40, 40)) 
        
        self.rect = self.image.get_rect()
        
        self.rect.center = (456, 399)

        
class Calango(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./sprites/coletaveis/calango.png")
        
        self.image = pygame.transform.scale(self.image, (40, 40)) 
        
        self.rect = self.image.get_rect()
        
        self.rect.center = (92, 153)
