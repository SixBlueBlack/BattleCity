import pygame
from base import base
from bullet import Bullet
from direction_type import Direction


class Tank(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.animation_state = 0
        self.image = base.sprites["player"][Direction.UP][0]
        self.rect = self.image.get_rect()
        self.bullet_existed = False
        self.rect.topleft = (pos_x * base.SPRITE_SIZE, pos_y * base.SPRITE_SIZE)
        self.direction = Direction.UP

    def update(self) -> None:
        i = 0
        if base.pressed:
            self.animation_state = (self.animation_state + 1) % 4
            if base.pressed:
                self.direction = base.pressed
            self.image = base.sprites["player"][base.pressed][self.animation_state // 2]
        i += 1
        if base.pressed == Direction.DOWN:
            self.rect.y += 1
            sprite = pygame.sprite.spritecollide(self, base.tile_sprites, False)
            if sprite or self.rect.y > base.HEIGHT - base.SPRITE_SIZE + 8:
                self.rect.y -= 1
        if base.pressed == Direction.UP:
            self.rect.y -= 1
            sprite = pygame.sprite.spritecollide(self, base.tile_sprites, False)
            if sprite or self.rect.y < 0:
                self.rect.y += 1
        if base.pressed == Direction.LEFT:
            self.rect.x -= 1
            sprite = pygame.sprite.spritecollide(self, base.tile_sprites, False)
            if sprite or self.rect.x < 0:
                self.rect.x += 1
        if base.pressed == Direction.RIGHT:
            self.rect.x += 1
            sprite = pygame.sprite.spritecollide(self, base.tile_sprites, False)
            if sprite or self.rect.x > base.WIDTH - base.SPRITE_SIZE + 8:
                self.rect.x -= 1

    def shoot(self) -> None:
        if self.bullet_existed:
            return
        self.bullet_existed = True
        if self.direction == Direction.UP:
            bullet = Bullet(self.rect.centerx, self.rect.top, self.direction, self)
        elif self.direction == Direction.DOWN:
            bullet = Bullet(self.rect.centerx, self.rect.bottom, self.direction, self)
        elif self.direction == Direction.LEFT:
            bullet = Bullet(self.rect.left, self.rect.centery, self.direction, self)
        else:
            bullet = Bullet(self.rect.right, self.rect.centery, self.direction, self)
        base.all_sprites.add(bullet)
        base.bullets.add(bullet)
