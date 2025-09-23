import pygame
import sys
from Player import Player

pygame.init()
screenX, screenY = 800, 800
gameScreen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Platformer")

tickSpeed = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player(pos=(100, 800), size=64)
all_sprites.add(player)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    gameScreen.fill((244, 194, 194))
    all_sprites.draw(gameScreen)
    pygame.display.flip()
    tickSpeed.tick(60)
pygame.quit()
sys.exit()
