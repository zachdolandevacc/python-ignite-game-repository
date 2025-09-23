import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size, playernum):
        super().__init__()
        self.playernum = playernum
        if(self.playernum == 1):
            imgPath = 'Player_1_Blue.png'
        elif(self.playernum == 2):
            imgPath = 'Player_2_Purple.png'
        self.image = pygame.image.load(imgPath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.jumpSpeed = -15
        self.facingRight = True
        self.onGround = True 
        self.jumpCooldown = 0
        self.health = 3
        self.respawn_position = pos

    def getInput(self):
        keys = pygame.key.get_pressed()
        if(self.playernum == 1):
            if keys[pygame.K_w]:
                self._jump()
            if keys[pygame.K_a]:
                self.direction.x = -1
                self.facingRight = False
            elif keys[pygame.K_d]:
                self.direction.x = 1
                self.facingRight = True
            else:
                self.direction.x = 0

        if(self.playernum == 2):
            if keys[pygame.K_u]:
                self._jump()
            if keys[pygame.K_h]:
                self.direction.x = -1
                self.facingRight = False
            elif keys[pygame.K_k]:
                self.direction.x = 1
                self.facingRight = True
            else:
                self.direction.x = 0

        if(self.playernum == 3):
            if keys[pygame.K_UP]:
                self._jump()
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.facingRight = False
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.facingRight = True
            else:
                self.direction.x = 0

    def _jump(self):
        if self.onGround and self.jumpCooldown == 0:
            self.direction.y = self.jumpSpeed
            self.onGround = False
            self.jumpCooldown = 45

    def respawn(self):
        self.rect.topleft = self.respawn_position

    def update(self):
        self.getInput()
        if self.jumpCooldown > 0:
            self.jumpCooldown -= 1
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y
        if not self.onGround:
            self.direction.y += 1
        if self.rect.bottom >= 800:
            self.rect.bottom = 800
            self.direction.y = 0
            self.onGround = True
