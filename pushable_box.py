import pygame

class PushableBox(pygame.sprite.Sprite):
    def __init__(self, pos, size=64, color=(200, 50, 50)):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.velocity = pygame.math.Vector2(0, 0)
        self.friction = 0.8

    def update(self):
        # Apply velocity
        self.rect.x += int(self.velocity.x)
        self.rect.y += int(self.velocity.y)
        # Apply friction to slow down
        self.velocity.x *= self.friction
        self.velocity.y *= self.friction
        # Stop if velocity is very low
        if abs(self.velocity.x) < 0.1:
            self.velocity.x = 0
        if abs(self.velocity.y) < 0.1:
            self.velocity.y = 0

        # Always apply gravity
        self.velocity.y += 1  # Simple gravity
        # Prevent falling through the floor
        if self.rect.bottom >= 850:
            self.rect.bottom = 850
            self.velocity.y = 0
