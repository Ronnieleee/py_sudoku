# -*- coding: utf-8 -*-
# /usr/bin/python3

"""
By Ronnieleee ronnie.lee@foxmail.com.
https://github.com/Ronnieleee/py_sudoku.git
"""

import numpy as np
from py_sudoku import Sudoku
from random import seed


def main():
    seed(1)
    """
    board = [[0, 3, 9, 2, 5, 8, 4, 1, 7],
             [4, 5, 7, 3, 1, 9, 8, 6, 2],
             [2, 8, 1, 7, 4, 6, 9, 5, 3],
             [5, 9, 3, 6, 2, 4, 0, 7, 8],
             [8, 2, 4, 5, 7, 1, 3, 9, 6],
             [1, 7, 0, 8, 0, 3, 2, 4, 5],
             [7, 4, 2, 9, 8, 5, 6, 3, 1],
             [3, 1, 5, 4, 6, 2, 7, 8, 9],
             [9, 6, 8, 1, 3, 7, 5, 2, 4]]


        board = 
            [[6, 3, 9, 2, 5, 8, 4, 1, 7],
             [4, 5, 7, 3, 1, 9, 8, 6, 2],
             [2, 8, 1, 7, 4, 6, 9, 5, 3],
             [5, 9, 3, 6, 2, 4, 1, 7, 8],
             [8, 2, 4, 5, 7, 1, 3, 9, 6],
             [1, 7, 6, 8, 9, 3, 2, 4, 5],
             [7, 4, 2, 9, 8, 5, 6, 3, 1],
             [3, 1, 5, 4, 6, 2, 7, 8, 9],
             [9, 6, 8, 1, 3, 7, 5, 2, 4]]
    """

    # problem = Sudoku(board=np.array(board, dtype=int))
    problem = Sudoku()
    # problem.sudoku_solver()
    fuck1 = problem.board
    print(fuck1)
    print("After generator")
    problem.generator()
    fuck2 = problem.board
    print(fuck2)
    print("After Solver")
    problem.solver()
    fuck3 = problem.board
    print(fuck3)

    print(np.equal(fuck3, fuck1).all())


if __name__ == "__main__":
    main()
