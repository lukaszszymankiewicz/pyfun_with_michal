import pygame

def init_game():
    pygame.init()


def init_window(x, y, name):
    win = pygame.display.set_mode((x, y))
    pygame.display.set_caption(name)

    return win

def control_framerate():
    pygame.time.delay(50)

