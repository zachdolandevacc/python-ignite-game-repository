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
            
        # Player and box collision logic
    if player.rect.colliderect(box.rect):
        # Push box horizontally if player moves into it
        if player.direction.x > 0 and player.rect.right > box.rect.left:
            box.velocity.x = player.speed
        elif player.direction.x < 0 and player.rect.left < box.rect.right:
            box.velocity.x = -player.speed

    all_sprites.update()

    # --- Collision: Player standing on box ---
    # Check if player is falling and lands on top of the box
    if player.rect.colliderect(box.rect):
        # Calculate previous position (simulate one frame back)
        prev_bottom = player.rect.bottom - player.direction.y
        # If player's bottom was above the box and now collides, place player on top
        if prev_bottom <= box.rect.top and player.direction.y >= 0:
            player.rect.bottom = box.rect.top
            player.direction.y = 0
            player.onGround = True
    
    all_sprites.update()
    gameScreen.fill((0, 0, 0))
    all_sprites.draw(gameScreen)
    pygame.display.flip()
    tickSpeed.tick(60)
    
pygame.quit()
sys.exit()
