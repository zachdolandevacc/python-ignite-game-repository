import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        imgPath = 'Player_1_Blue.png'
        self.image = pygame.image.load(imgPath).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.jumpSpeed = -15
        self.facingRight = True
        self.onGround = True
        self.jumpCooldown = 0
        self.is_dead = False
        self.invincible = False
        self.invincibility_timer = 0

    def getInput(self):
        if not self.is_dead:
            keys = pygame.key.get_pressed()
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

    def update(self):
        if not self.is_dead:
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
            if self.invincible:
                self.invincibility_timer -= 1
                if self.invincibility_timer <= 0:
                    self.invincible = False
