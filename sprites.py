import pygame
import os
from direction_type import Direction


def load_image(name: str, colorkey=None) -> pygame.Surface:  # Загрузка картинок
    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def get_sprites():
    sprites = {"player": {Direction.UP: [pygame.transform.scale(load_image('tankUp1.png'), (39, 39)),
                                         pygame.transform.scale(load_image('tankUp2.png'), (39, 39))],
                          Direction.DOWN: [pygame.transform.scale(load_image('tankDown1.png'), (39, 39)),
                                           pygame.transform.scale(load_image('tankDown2.png'), (39, 39))],
                          Direction.LEFT: [pygame.transform.scale(load_image('tankLeft1.png'), (39, 39)),
                                           pygame.transform.scale(load_image('tankLeft2.png'), (39, 39))],
                          Direction.RIGHT: [pygame.transform.scale(load_image('tankRight1.png'), (39, 39)),
                                            pygame.transform.scale(load_image('tankRight2.png'), (39, 39))]},
               "tiles": {"brick": pygame.transform.scale(load_image('Bricks.png'), (48, 48)),
                         "notBreakable": pygame.transform.scale(load_image('NotBreakable.png'), (48, 48)),
                         "water": pygame.transform.scale(load_image("Water.png"), (48, 48)),
                         "grass": pygame.transform.scale(load_image("Grass.png"), (48, 48)),
                         "base": pygame.transform.scale(load_image("Base.png"), (48, 48))},
               "bullet": {Direction.UP: pygame.transform.scale(load_image('bulletUp.png'), (6, 8)),
                          Direction.DOWN: pygame.transform.scale(load_image('bulletDown.png'), (6, 8)),
                          Direction.LEFT: pygame.transform.scale(load_image('bulletLeft.png'), (8, 6)),
                          Direction.RIGHT: pygame.transform.scale(load_image('bulletRight.png'), (8, 6))}
               }
    return sprites
