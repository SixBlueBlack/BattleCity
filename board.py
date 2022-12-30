from tiles import *
from typing import List
from tank import Tank


def load_level(filename: str) -> List[str]:
    filename = "levels/" + filename
    with open(filename, 'r') as mapFile:
        level_map = list(map(str.strip, mapFile.readlines()))
    return level_map


class Board:
    def __init__(self) -> None:
        self.board = []
        self.tank = None

    def load(self, level_name: str) -> None:
        lev = load_level(level_name)
        for el in lev:
            self.board.append(list(el))
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == '#':
                    self.board[i][j] = Brick(j, i)
                elif self.board[i][j] == 'W':
                    self.board[i][j] = Water(j, i)
                elif self.board[i][j] == 'N':
                    self.board[i][j] = NotBreakable(j, i)
                elif self.board[i][j] == 'G':
                    self.board[i][j] = Grass(j, i)
                elif self.board[i][j] == 'B':
                    self.board[i][j] = Base(j, i)
                elif self.board[i][j] == 'P':
                    self.board[i][j] = None
                    self.tank = Tank(j, i)
                    base.all_sprites.add(self.tank)
                elif self.board[i][j] == '.':
                    self.board[i][j] = None


board = Board()
