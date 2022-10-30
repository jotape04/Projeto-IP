import pygame, sys
from shooter import Shooter
import time

pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))

player = Shooter()
player_group = pygame.sprite.Group()
player_group.add(player)
pygame.mouse.set_visible(False)

bullet_group = pygame.sprite.Group()

now = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if 1.1 > time.time() - now > 0.9:
        player.wait()

    if 1.8 > time.time() - now > 1.6:
        player.prepare()

    if 2.1 > time.time() - now > 1.9:
        now = time.time()
        bullet_group.add(player.createb())
    
    
    
    screen.fill((30,30,30))
    bullet_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    bullet_group.update(screen_width)
    clock.tick(60)
