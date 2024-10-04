import pygame

from util import init_game, init_window, control_framerate
from globals import WINDOW_W, WINDOW_H, NAME, BLUE, GREEN
from hero import Hero
from tile import Tile


def run():

    # init game
    init_game()
    win = init_window(WINDOW_W, WINDOW_H, NAME)

    # init level
    hero = Hero(50, 400, 50, 60)
    tiles = [
        Tile(50, 460, BLUE),
        Tile(82, 460, BLUE),
        Tile(114, 460, BLUE),
        Tile(146, 460, BLUE),
        Tile(178, 460, BLUE),
        Tile(114, 250, GREEN)
    ]

    # main loop
    while True:
        control_framerate()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # control the player
        keys = pygame.key.get_pressed()
        hero.control(keys)

        # check for collisions
        hero.collisions(tiles)

        # draw empty canvas color
        win.fill((32, 125, 32))

        # draw everything
        hero.draw(win)
        for tile in tiles:
            tile.draw(win)

        # update the window
        pygame.display.update()

run()