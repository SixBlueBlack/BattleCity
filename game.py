import pygame
import os
from typing import List
from os.path import isfile, join
from base import base
from tank import Tank
from board import Board
from direction_type import Direction


class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.menu_button = 1

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.tank.shoot()
                if event.key in [direction_type.value for direction_type in Direction]:
                    base.pressed = Direction(event.key)
            if base.pressed and event.type == pygame.KEYUP:
                if event.key == base.pressed.value:
                    base.pressed = None

    def start(self) -> None:
        self.show_main_menu()
        while True:
            self.check_events()
            self.update_screen()

    def show_main_menu(self) -> None:
        choosing = True
        self.draw_main_menu()
        while choosing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.menu_button == 2:
                            self.menu_button = 1
                            self.draw_main_menu()
                    elif event.key == pygame.K_DOWN:
                        if self.menu_button == 1:
                            self.menu_button = 2
                            self.draw_main_menu()
                    elif event.key == pygame.K_RETURN:
                        choosing = False
            base.clock.tick(60)
        self.choose_level()

    @staticmethod
    def get_level_names() -> List[str]:
        dir_path = os.path.dirname(os.path.realpath(__file__)) + "/levels"
        return [f for f in os.listdir(dir_path) if isfile(join(dir_path, f))]

    def choose_level(self):
        choosing = True
        level_number = 0
        level_names = self.get_level_names()
        self.draw_level_menu(level_names[level_number])
        while choosing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and level_number > 0:
                        level_number -= 1
                        self.draw_level_menu(level_names[level_number])
                    if event.key == pygame.K_RIGHT and level_number < len(level_names) - 1:
                        level_number += 1
                        self.draw_level_menu(level_names[level_number])
                    if event.key == pygame.K_RETURN:
                        choosing = False
            base.clock.tick(60)
        self.start_game(level_names[level_number])

    def start_game(self, level_name: str) -> None:
        self.board.load(level_name)

    def draw_level_menu(self, level_name: str) -> None:
        base.screen.fill((128, 128, 128))
        level_name = base.font.render(level_name.split('.')[0], True, (0, 0, 0))
        text_rect = level_name.get_rect(center=(base.WIDTH / 2, base.HEIGHT / 2))
        base.screen.blit(level_name, text_rect)
        pygame.display.flip()

    def draw_main_menu(self) -> None:
        base.screen.fill((0, 0, 0))
        base.screen.blit(base.font.render("1 PLAYER", True, (255, 255, 255)), (165, 250))
        base.screen.blit(base.font.render("2 PLAYERS", True, (255, 255, 255)), (165, 275))
        tank_sprite = base.sprites["player"][Direction.RIGHT][0]
        if self.menu_button == 1:
            base.screen.blit(tank_sprite, [125, 245])
        elif self.menu_button == 2:
            base.screen.blit(tank_sprite, [125, 270])

        pygame.display.flip()

    @staticmethod
    def update_screen() -> None:
        base.screen.fill((0, 0, 0))
        base.all_sprites.update()
        base.all_sprites.draw(base.screen)
        pygame.display.update()
        base.clock.tick(60)
