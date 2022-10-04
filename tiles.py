import pygame
from settings import sprites


class Board:
    def __init__(self):
        pass


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Brick(Tile):
    def __init__(self):
        super().__init__()


class Water(Tile):
    def __init__(self):
        super().__init__()


class NotBreakable(Tile):
    def __init__(self):
        super().__init__()
