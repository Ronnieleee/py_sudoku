from random import shuffle, seed
# import numpy as np

class _SudokuSolver:
    def __init__(self, sudoku):
        self.width = sudoku.width
        self.height = sudoku.height
        self.size = sudoku.size
        self.sudoku = sudoku

    def _solve(self, raising=False):
        blanks = self.__get_blanks()
        blank_count = len(blanks)

    def __get_blanks(self):
        blanks = []
        for i, row in enumerate(self.sudoku.board):
            for j, cell in enumerate(row):
                if cell == Sudoku._empty_cell_value:
                    blanks += [(i, j)]
        return blanks


class Sudoku:
    _empty_cell_value = None

    def __init__(self, width=3, height=None, board=None, difficulty=-1, seeds=1):
        self.board = board
        self.width = width
        self.height = height
        if not height:
            self.height = width
        self.size = self.width * self.height
        self.__difficulty = difficulty

        assert self.width > 0, "Width must be 1 or above"
        assert self.height > 0, "Height must be 1 or above"
        assert self.size > 1, "Board must be greater than 1 X 1"

        if board:
            blank_count = 0
            for row in self.board:
                for i in range(len(row)):
                    if not row[i] in range(1, self.size + 1):
                        row[i] = Sudoku._empty_cell_value
                        blank_count += 1
            if difficulty == -1:
                self.__difficulty = blank_count / self.size / self.size
        else:
            positions = list(range(self.size))
            seed(seeds)
            shuffle(positions)
            self.board = [[(i + 1) if i == positions[j] else
                           Sudoku._empty_cell_value for i in range(self.size)] for j in range(self.size)]

    def solve(self, raising=True):
        return _SudokuSolver(self)._solve(raising)

    def difficulty(self, difficulty):
        assert 0 < difficulty < 1, "Difficulty must be between 0 and 1"
        indices = list(range(self.size * self.size))
        shuffle(indices)
        problem_board = self.solve.board()
        for index in indices[: int(difficulty * self.size * self.size)]:
            row_index = index // self.size
            col_index = index % self.size
            problem_board[row_index][col_index] = Sudoku._empty_cell_value
        return Sudoku(self.width, self.height, problem_board, difficulty)




def main():


if __name__ == "__main__":
    main()
