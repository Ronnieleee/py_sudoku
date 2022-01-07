# -*- coding: utf-8 -*-
# /usr/bin/python3

# By Ronnieleee ronnie.lee@foxmail.com. https://github.com/Ronnieleee/py_sudoku.git

from random import shuffle
import numpy as np


class Sudoku:
    _empty_cell_value = 0

    def __init__(self, width: int = 3, height: int = 3, board: [[]] = None, difficulty: float = 0.5):
        """ Random Create The Whole Sudoku.

            Keyword arguments:
            width:int         --- the width of the Block (default 3).
            height:int        --- the height of the Block (default 3).
            board:ndarray     --- the ndarray to store the data.
            difficulty: float --- determine the numbers of the holes to be dug (default 0.5) holes / board.Size.
            Returns:

        """
        self.width = width
        self.height = height
        self.size = self.width * self.height
        self.__difficulty = difficulty

        assert self.width > 0, 'Width cannot be less than 1'
        assert self.height > 0, 'Height cannot be less than 1'
        assert self.size > 1, 'Board size cannot be 1 x 1'

        if board is None:
            self.board = np.zeros((self.size, self.size), dtype=int)
            self.__generator()
        else:
            self.board = board

    def generator(self):
        """ Random Create The Sudoku Puzzle.

            Keyword arguments:
            create the puzzle by digging the holes and check the puzzle has only one ans.
            Returns:

        """
        randomlist = list(range(self.board.size))
        shuffle(randomlist)
        self.__dig_holes(randomlist, int(self.board.size*self.__difficulty))

    def solver(self):
        """ Solver The Sudoku Puzzle.

            Keyword argument:

            Returns: True for succeed False for fail

        """
        if self.__solver():
            return True
        else:
            print("UnsolvableSudoku")
            return False

    def difficulty(self, difficulty: float = 0.5):
        """ Set The Difficulty Of The Sudoku Puzzle.
            if you chose to use this function. you must use it before generator().
            Keyword argument:
            difficulty: float   --- holes / board.Size (default 0.5).
            Returns:

        """
        self.__difficulty = difficulty

    def __possible_value_at_position(self, row: int, col: int):
        """
        Get The Possible Numbers.
        :param row: int (row number)
        :param col: int (col number)
        :return: set() (the set of the remaining numbers)
        """
        r = row//self.width*self.width
        c = col//self.height*self.height
        numberset = set(range(1, self.size+1))
        return numberset.difference(set(self.board[r:r+self.width, c:c+self.height].flat)).difference(
            set(self.board[row, :])).difference(set(self.board[:, col]))

    def __generator(self, n: int = 0):
        """
        Private Function To Generator The Whole Sudoku.
        :param n: int = 0 (start place)
        :return: True for succeed False for fail
        """
        if n == self.board.size:
            return True
        (row, col) = divmod(n, self.size)
        if self.board[row][col] > 0:
            if self.__generator(n+1):
                return True
        else:
            remainders = list(self.__possible_value_at_position(row, col))
            shuffle(remainders)
            for v in remainders:
                self.board[row][col] = v
                if self.__generator(n+1):
                    return True
                self.board[row][col] = 0
        return False

    def __solver(self, n: int = 0):
        """
        Private Function To Solver The Sudoku Puzzle.
        :param n: int = 0 (start place)
        :return: True for succeed False for fail
        """
        if n == self.board.size:
            return True
        (row, col) = divmod(n, self.size)
        if self.board[row][col] > 0:
            if self.__solver(n + 1):
                return True
        else:
            remainders = list(self.__possible_value_at_position(row, col))
            for v in remainders:
                self.board[row][col] = v
                if self.__solver(n + 1):
                    return True
                self.board[row][col] = 0
        return False

    def __solution_count(self, n: int = 0, nof_solution: int = 0):
        """
        Count The Possible Solutions.
        :param n: int = 0 start place
        :param nof_solution: int = 0 solution count
        :return: int (the solution count)
        """
        if nof_solution > 1:
            return nof_solution
        if n >= self.board.size:
            nof_solution += 1
            return nof_solution
        (row, col) = divmod(n, self.size)
        if self.board[row][col] > 0:
            nof_solution = self.__solution_count(n+1, nof_solution)
        else:
            fuckedlist = self.__possible_value_at_position(row, col)
            for v in fuckedlist:
                self.board[row][col] = v
                nof_solution = self.__solution_count(n+1, nof_solution)
                self.board[row][col] = 0
        return nof_solution

    def __dig_holes(self, randomlist: [], n: int = 0):
        """
        Dig The Holes To Generator The Sudoku Puzzle.
        :param randomlist: [] (the digging point)
        :param n: int (start place) (default 0)
        :return: None
        """
        if n >= self.board.size:
            return
        (row, col) = divmod(randomlist[n], self.size)
        fuck = self.board[row][col]
        if fuck > 0:
            self.board[row][col] = Sudoku._empty_cell_value
            nof_solution = self.__solution_count()
            if nof_solution == 1:
                self.board[row][col] = 0
            else:
                self.board[row][col] = fuck
        self.__dig_holes(randomlist, n+1)
