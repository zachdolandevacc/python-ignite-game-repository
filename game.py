import pygame
import sys
import random
import math

# Initialization
pygame.init()
screenX = 900
screenY = 900
gameScreen = pygame.display.set_mode((screenX, screenY))
tickSpeed = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    gameScreen.fill((0, 0, 0))
    pygame.display.flip()
    tickSpeed.tick(60)
