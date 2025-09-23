import pygame
import sys
from player import Player
from pushable_box import PushableBox

pygame.init()
screenX, screenY = 900, 900
gameScreen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("Platformer")

tickSpeed = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
playerOne = Player(pos=(100, 850), size=64, playernum=1)
playerTwo = Player(pos=(300, 850), size=64, playernum=2)
playerThree = Player(pos=(500, 850), size=64, playernum=3)
box = PushableBox(pos=(400, 700), size=64)
all_sprites.add(playerOne)
all_sprites.add(playerTwo)
all_sprites.add(playerThree)
all_sprites.add(box)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    gameScreen.fill((0, 0, 0))
    all_sprites.draw(gameScreen)
    pygame.display.flip()
    tickSpeed.tick(60)
    
pygame.quit()
sys.exit()
