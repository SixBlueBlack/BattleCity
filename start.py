import pygame


class Base:
    def __init__(self):
        self.HEIGHT = 600
        self.WIDTH = 800
        self.SPRITE_SIZE = 16
        pygame.init()
        self.screen = pygame.display.set_mode((624, 624))
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.pressed = ""


base = Base()
