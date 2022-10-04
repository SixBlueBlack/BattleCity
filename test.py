import pygame
from settings import sprites

HEIGHT = 600
WIDTH = 800
SPRITE_SIZE = 16
pygame.init()
screen = pygame.display.set_mode((624, 624))
clock = pygame.time.Clock()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.image = sprites["bullet"][direction]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 2

    def update(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        if self.direction == 'down':
            self.rect.y += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.rect.bottom < 0 or self.rect.bottom > 624 or self.rect.left < 0 or self.rect.right > 624:
            self.kill()


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprites["player"]["up"][0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.direction = 'up'

    def update(self) -> None:
        global pressed, animation_state
        i = 0
        if pressed:
            animation_state = (animation_state + 1) % 4
            if pressed:
                self.direction = pressed
            # self.image = animation_frames_list[i]
            self.image = sprites["player"][pressed][animation_state // 2]
        i += 1
        if pressed == "down":
            self.rect.y += 1
        if pressed == "up":
            self.rect.y -= 1
        if pressed == "left":
            self.rect.x -= 1
        if pressed == "right":
            self.rect.x += 1
        # pressed = ""

    def shoot(self):
        if self.direction == 'up':
            bullet = Bullet(self.rect.centerx, self.rect.top, self.direction)
        elif self.direction == 'down':
            bullet = Bullet(self.rect.centerx, self.rect.bottom, self.direction)
        elif self.direction == 'left':
            bullet = Bullet(self.rect.left, self.rect.centery, self.direction)
        else:
            bullet = Bullet(self.rect.right, self.rect.centery, self.direction)
        all_sprites.add(bullet)
        bullets.add(bullet)


animation_state = 0
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
tank = Tank()
all_sprites.add(tank)
pressed = ""
# animation_frames_list = get_tank_sprites_dict()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tank.shoot()
            if event.key == pygame.K_RIGHT:
                pressed = 'right'
            if event.key == pygame.K_LEFT:
                pressed = 'left'
            if event.key == pygame.K_UP:
                pressed = 'up'
            if event.key == pygame.K_DOWN:
                pressed = 'down'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and pressed == 'right' or \
                    event.key == pygame.K_LEFT and pressed == 'left' or \
                    event.key == pygame.K_UP and pressed == 'up' or \
                    event.key == pygame.K_DOWN and pressed == 'down':
                pressed = ''

    screen.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.update()
    clock.tick(60)
    # all_sprites.update()
    # pygame.display.update()
