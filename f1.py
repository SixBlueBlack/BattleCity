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

# def get_tank_sprites_dict():
# animation_frames = []
# image = pygame.transform.scale(load_image("tankSprites.png"), (256, 256))
# for tank_type_i in range(2):
# for tank_type_j in range(2):
# for tank_level in range(8):
# for dimension in range(4):
# for animation in range(2):
# animation_frames.append(image.subsurface(pygame.Rect(
# tank_type_i * SPRITE_SIZE * 8 + dimension * SPRITE_SIZE * 2 + animation * SPRITE_SIZE,
# tank_type_j * SPRITE_SIZE * 8 + tank_level * SPRITE_SIZE, SPRITE_SIZE, SPRITE_SIZE)))
# row = 0
# for j in range(int(16)):
# for i in range(int(16)):
# animation_frames.append(image.subsurface(pygame.Rect(i * SPRITE_SIZE, row, SPRITE_SIZE, SPRITE_SIZE)))
# row += int(SPRITE_SIZE)
# return animation_frames
