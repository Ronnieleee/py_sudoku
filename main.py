# import random
from random import shuffle, seed
# import sys
import numpy as np


class Sudoku:
    def __init__(self):
        self.puzzle = np.zeros((9, 9), dtype=int)
        self.sudoku_generator(0)

    def possible_value_at_position(self, row: int, col: int):
        r = row//3*3
        c = col//3*3
        return {1, 2, 3, 4, 5, 6, 7, 8, 9}.difference(set(self.puzzle[r:r+3, c:c+3].flat)).difference(
            set(self.puzzle[row, :])).difference(set(self.puzzle[:, col]))

    def sudoku_generator(self, n: int):
        if n == 81:
            return True
        (row, col) = divmod(n, 9)
        if self.puzzle[row][col] > 0:
            if self.sudoku_generator(n+1):
                return True
        else:
            remainders = list(self.possible_value_at_position(row, col))
            shuffle(remainders)
            for v in remainders:
                self.puzzle[row][col] = v
                if self.sudoku_generator(n+1):
                    return True
                self.puzzle[row][col] = 0
        return False

    def solution_count(self, n: int, nof_solution: int):
        if nof_solution > 1:
            return nof_solution
        if n >= 81:
            nof_solution += 1
        (row, col) = divmod(n, 9)
        if self.puzzle[row][col] > 0:
            nof_solution = self.solution_count(n+1, nof_solution)
        else:
            fuckedlist = self.possible_value_at_position(row, col)
            for v in fuckedlist:
                self.puzzle[row][col] = v
                nof_solution = self.solution_count(n+1, nof_solution)
                self.puzzle[row][col] = 0
        return nof_solution

    def dig_holes(self, randomlist: [], n: int):
        if n >= 81:
            return
        (row, col) = divmod(randomlist[n], 9)
        fuck = self.puzzle[row][col]
        if fuck > 0:
            self.puzzle[row][col] = 0
            nof_solution = self.solution_count(0, 0)
            if nof_solution == 1:
                self.puzzle[row][col] = 0
            else:
                self.puzzle[row][col] = fuck
        self.dig_holes(randomlist, n+1)


def main():
    seed(1)
    problem = Sudoku()
    print(problem.puzzle)
    randomlist = list(range(81))
    shuffle(randomlist)
    problem.dig_holes(randomlist, 0)
    print("After")
    print(problem.puzzle)


if __name__ == "__main__":
    main()
