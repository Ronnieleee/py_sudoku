from random import shuffle, seed
import numpy as np


class Sudoku:
    _empty_cell_value = 0

    def __init__(self, width=3, height=None, board=None, difficulty=0.5):
        self.width = width
        self.height = height
        if not height:
            self.height = width
        self.size = self.width * self.height
        self.__difficulty = difficulty

        assert self.width > 0, 'Width cannot be less than 1'
        assert self.height > 0, 'Height cannot be less than 1'
        assert self.size > 1, 'Board size cannot be 1 x 1'

        if board is None:
            self.board = np.zeros((self.size, self.size), dtype=int)
            self.sudoku_generator()
        else:
            self.board = board

    def generator(self):
        randomlist = list(range(self.board.size))
        shuffle(randomlist)
        self.dig_holes(randomlist, int(self.board.size*self.__difficulty))

    def solver(self):
        self.sudoku_solver()

    def difficulty(self, difficulty: float = 0.5):
        self.__difficulty = difficulty

    def possible_value_at_position(self, row: int, col: int):
        r = row//self.width*self.width
        c = col//self.height*self.height
        numberset = set(range(1, self.size+1))
        return numberset.difference(set(self.board[r:r+self.width, c:c+self.height].flat)).difference(
            set(self.board[row, :])).difference(set(self.board[:, col]))

    def sudoku_generator(self, n: int = 0):
        if n == self.board.size:
            return True
        (row, col) = divmod(n, self.size)
        if self.board[row][col] > 0:
            if self.sudoku_generator(n+1):
                return True
        else:
            remainders = list(self.possible_value_at_position(row, col))
            shuffle(remainders)
            for v in remainders:
                self.board[row][col] = v
                if self.sudoku_generator(n+1):
                    return True
                self.board[row][col] = 0
        return False

    def sudoku_solver(self, n: int = 0):
        if n == self.board.size:
            return True
        (row, col) = divmod(n, self.size)
        if self.board[row][col] > 0:
            if self.sudoku_solver(n + 1):
                return True
        else:
            remainders = list(self.possible_value_at_position(row, col))
            for v in remainders:
                self.board[row][col] = v
                if self.sudoku_solver(n + 1):
                    return True
                self.board[row][col] = 0
        return False

    def solution_count(self, n: int = 0, nof_solution: int = 0):
        if nof_solution > 1:
            return nof_solution
        if n >= self.board.size:
            nof_solution += 1
            return nof_solution
        (row, col) = divmod(n, self.size)
        if self.board[row][col] > 0:
            nof_solution = self.solution_count(n+1, nof_solution)
        else:
            fuckedlist = self.possible_value_at_position(row, col)
            for v in fuckedlist:
                self.board[row][col] = v
                nof_solution = self.solution_count(n+1, nof_solution)
                self.board[row][col] = 0
        return nof_solution

    def dig_holes(self, randomlist: [], n: int = 0):
        if n >= self.board.size:
            return
        (row, col) = divmod(randomlist[n], self.size)
        fuck = self.board[row][col]
        if fuck > 0:
            self.board[row][col] = Sudoku._empty_cell_value
            nof_solution = self.solution_count()
            if nof_solution == 1:
                self.board[row][col] = 0
            else:
                self.board[row][col] = fuck
        self.dig_holes(randomlist, n+1)