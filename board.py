import os
import pygame


def load_image(name, colorkey=None):  # Загрузка картинок
    fullname = os.path.join('sprites', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
