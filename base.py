import pygame
from sprites import get_sprites


class Base:
    def __init__(self) -> None:
        self.HEIGHT = 624
        self.WIDTH = 624
        self.SPRITE_SIZE = 48
        pygame.init()
        self.screen = pygame.display.set_mode((self.HEIGHT, self.WIDTH))
        self.sprites = get_sprites()
        self.font = pygame.font.SysFont('arial', 24)
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.tile_sprites = pygame.sprite.Group()
        self.pressed = ""


base = Base()
