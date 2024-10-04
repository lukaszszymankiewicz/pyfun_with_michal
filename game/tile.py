import pygame


class Tile:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.width = 32
        self.height = 32

        self.color = color

    @property
    def shape(self):
        return self.x, self.y, self.width, self.height

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.shape)

