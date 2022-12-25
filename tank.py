import pygame
from start import base
from settings import sprites
from bullet import Bullet
from direction_type import Direction


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animation_state = 0
        self.image = sprites["player"][Direction.UP][0]
        self.rect = self.image.get_rect()
        self.rect.center = (base.WIDTH / 2, base.HEIGHT / 2)
        self.direction = Direction.UP

    def update(self) -> None:
        i = 0
        if base.pressed:
            self.animation_state = (self.animation_state + 1) % 4
            if base.pressed:
                self.direction = base.pressed
            self.image = sprites["player"][base.pressed][self.animation_state // 2]
        i += 1
        if base.pressed == Direction.DOWN:
            self.rect.y += 1
        if base.pressed == Direction.UP:
            self.rect.y -= 1
        if base.pressed == Direction.LEFT:
            self.rect.x -= 1
        if base.pressed == Direction.RIGHT:
            self.rect.x += 1

    def shoot(self):
        if self.direction == Direction.UP:
            bullet = Bullet(self.rect.centerx, self.rect.top, self.direction)
        elif self.direction == Direction.DOWN:
            bullet = Bullet(self.rect.centerx, self.rect.bottom, self.direction)
        elif self.direction == Direction.LEFT:
            bullet = Bullet(self.rect.left, self.rect.centery, self.direction)
        else:
            bullet = Bullet(self.rect.right, self.rect.centery, self.direction)
        base.all_sprites.add(bullet)
        base.bullets.add(bullet)
