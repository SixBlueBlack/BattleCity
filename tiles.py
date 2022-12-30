import pygame
from base import base


class Tile(pygame.sprite.Sprite):
    def __init__(self, sprite: pygame.Surface, pos_x: int, pos_y: int) -> None:
        super().__init__(base.tile_sprites, base.all_sprites)
        self.image = sprite
        self.rect = self.image.get_rect().move(base.SPRITE_SIZE * pos_x, base.SPRITE_SIZE * pos_y)


class Brick(Tile):
    def __init__(self, pos_x: int, pos_y: int) -> None:
        super().__init__(base.sprites["tiles"]["brick"], pos_x, pos_y)


class Water(Tile):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__(base.sprites["tiles"]["water"], pos_x, pos_y)


class NotBreakable(Tile):
    def __init__(self, pos_x: int, pos_y: int) -> None:
        super().__init__(base.sprites["tiles"]["notBreakable"], pos_x, pos_y)


class Grass(Tile):
    def __init__(self, pos_x: int, pos_y: int) -> None:
        super().__init__(base.sprites["tiles"]["grass"], pos_x, pos_y)


class Base(Tile):
    def __init__(self, pos_x: int, pos_y: int) -> None:
        super().__init__(base.sprites["tiles"]["base"], pos_x, pos_y)
