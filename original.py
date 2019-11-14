import pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((500, 500))

background = (0x04, 0x92, 0xfc)
playerSprite = pygame.image.load("bird-scrub-jay.png").convert_alpha()

window.fill(background)
quit = False

while not quit:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True

    window.fill(background)
    window.blit(playerSprite, (0, 0))
    pygame.display.update()

window.blit(playerSprite, (0, 0))

pygame.quit()
