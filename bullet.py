import pygame
from base import base
from direction_type import Direction


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, direction: Direction, parent: pygame.sprite.Sprite) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.parent = parent
        self.direction = direction
        self.image = base.sprites["bullet"][direction]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3

    def update(self) -> None:
        self.move()

    def move(self) -> None:
        if self.direction == Direction.UP:
            self.rect.y -= self.speed
        if self.direction == Direction.DOWN:
            self.rect.y += self.speed
        if self.direction == Direction.LEFT:
            self.rect.x -= self.speed
        if self.direction == Direction.RIGHT:
            self.rect.x += self.speed
        if self.rect.bottom < 0 or self.rect.bottom > 624 or self.rect.left < 0 or self.rect.right > 624:
            self.die()

    def die(self) -> None:
        self.parent.bullet_existed = False
        self.kill()
