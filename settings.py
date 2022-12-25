import pygame
from board import load_image
from direction_type import Direction

sprites = {"player": {Direction.UP: [pygame.transform.scale(load_image('tankUp1.png'), (39, 39)),
                                     pygame.transform.scale(load_image('tankUp2.png'), (39, 39))],
                      Direction.DOWN: [pygame.transform.scale(load_image('tankDown1.png'), (39, 39)),
                                       pygame.transform.scale(load_image('tankDown2.png'), (39, 39))],
                      Direction.LEFT: [pygame.transform.scale(load_image('tankLeft1.png'), (39, 39)),
                                       pygame.transform.scale(load_image('tankLeft2.png'), (39, 39))],
                      Direction.RIGHT: [pygame.transform.scale(load_image('tankRight1.png'), (39, 39)),
                                        pygame.transform.scale(load_image('tankRight2.png'), (39, 39))]},
           "tiles": {"brick": pygame.transform.scale(load_image('Bricks.png'), (48, 48))},
           "bullet": {Direction.UP: pygame.transform.scale(load_image('bulletUp.png'), (6, 8)),
                      Direction.DOWN: pygame.transform.scale(load_image('bulletDown.png'), (6, 8)),
                      Direction.LEFT: pygame.transform.scale(load_image('bulletLeft.png'), (8, 6)),
                      Direction.RIGHT: pygame.transform.scale(load_image('bulletRight.png'), (8, 6))}
           }
