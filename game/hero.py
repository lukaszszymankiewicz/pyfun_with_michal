import pygame
from globals import RED

class Hero:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

        self.vel = 5
        self.jump = False
        self.jump_count = 10
        self.color = RED

    @property
    def shape(self):
        return self.x, self.y, self.width, self.height

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.shape)

    def control(self, keys):
        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel

        if keys[pygame.K_RIGHT] and self.x < 500 - self.width - self.vel:
            self.x += self.vel

        if not self.jump:
            if keys[pygame.K_SPACE]:
                self.jump = True
        else:
            if self.jump_count >= -10:
                direction = 1 if self.jump_count > 0 else -1
                self.y -= (self.jump_count ** 2) * 0.5 * direction
                self.jump_count -= 1
            else:
                self.jump = False
                self.jump_count = 10

    def collisions(self, colliders):
        for collider in colliders:
            if self.rect.colliderect(collider.rect):
                self.jump = False
                self.jump_count = -1
                self.y = collider.rect.y + collider.rect.h + 1

        # hero cannot move lower than the base level of 400
        if self.y > 400:
            self.y = 400
            self.jump = False
            self.jump_count = 10
