import pygame
from f1 import load_image

pygame.init()
screen = pygame.display.set_mode((624, 624))

sprites = {"player": {"up": [pygame.transform.scale(load_image('tankUp1.png'), (39, 39)),
                             pygame.transform.scale(load_image('tankUp2.png'), (39, 39))],
                      "down": [pygame.transform.scale(load_image('tankDown1.png'), (39, 39)),
                               pygame.transform.scale(load_image('tankDown2.png'), (39, 39))],
                      "left": [pygame.transform.scale(load_image('tankLeft1.png'), (39, 39)),
                               pygame.transform.scale(load_image('tankLeft2.png'), (39, 39))],
                      "right": [pygame.transform.scale(load_image('tankRight1.png'), (39, 39)),
                                pygame.transform.scale(load_image('tankRight2.png'), (39, 39))]},
           "tiles": {"brick": pygame.transform.scale(load_image('Bricks.png'), (48, 48))},
           "bullet": {"up": pygame.transform.scale(load_image('bulletUp.png'), (6, 8)),
                      "down": pygame.transform.scale(load_image('bulletDown.png'), (6, 8)),
                      "left": pygame.transform.scale(load_image('bulletLeft.png'), (8, 6)),
                      "right": pygame.transform.scale(load_image('bulletRight.png'), (8, 6))}
           }
