import pygame
from start import base
from tank import Tank
from direction_type import Direction


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tank.shoot()
            if event.key in [direction_type.value for direction_type in Direction]:
                base.pressed = Direction(event.key)
        if base.pressed and event.type == pygame.KEYUP:
            if event.key == base.pressed.value:
                base.pressed = None


def update_screen():
    base.screen.fill((0, 0, 0))
    base.all_sprites.update()
    base.all_sprites.draw(base.screen)
    pygame.display.update()
    base.clock.tick(60)


tank = Tank()
base.all_sprites.add(tank)
while True:
    check_events()
    update_screen()
