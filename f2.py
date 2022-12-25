from tiles import *


def load_level(filename):
    filename = "levels/" + filename
    with open(filename, 'r') as mapFile:
        level_map = list(map(str.strip, mapFile.readlines()))
    return level_map


class Board:  # Класс для работы с пошаговой частью игры
    def __init__(self):
        self.board = []

    def load(self):  # Перевод уровня из текстового файла в матрицу
        lev = load_level('test.txt')
        for el in lev:
            self.board.append(list(el))
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == '#':
                    self.board[i][j] = Brick()
                elif self.board[i][j] == 'W':
                    self.board[i][j] = Water()
                elif self.board[i][j] == 'N':
                    self.board[i][j] = NotBreakable()
                elif self.board[i][j] == 'B':
                    pass
                elif self.board[i][j] == '.':
                    self.board[i][j] = None


board = Board()
board.load()
