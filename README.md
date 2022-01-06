# py_sudoku
A Simple Library That Ramdom Create Sudoku Puzzles And Solve Them In Python
## install
pip install py_sudoku
# Usage
## basic usage generator the whole sudoku
```python
from py_sudoku import Sudoku
from random import seed
from numpy import equal
seed(1)
puzzle = Sudoku()
# Random create the whole Sudoku.
realans = puzzle.board
print(realans)

[[6 3 9 2 5 8 4 1 7]
 [4 5 7 3 1 9 8 6 2]
 [2 8 1 7 4 6 9 5 3]
 [5 9 3 6 2 4 1 7 8]
 [8 2 4 5 7 1 3 9 6]
 [1 7 6 8 9 3 2 4 5]
 [7 4 2 9 8 5 6 3 1]
 [3 1 5 4 6 2 7 8 9]
 [9 6 8 1 3 7 5 2 4]]
```


## create the sudoku puzzle
```python
# set the difficulty 0~1 recommand below 0.7.
puzzle.difficulty(0.6)
# get the sudoku puzzle by digging holes.
puzzle.generator()
problem = puzzle.board
print(problem)

[[6 0 9 2 5 8 0 0 0]
 [4 5 7 0 0 0 8 0 2]
 [2 0 0 0 4 0 0 5 0]
 [5 9 3 6 0 0 1 0 8]
 [8 0 0 5 7 0 3 9 0]
 [1 0 6 8 9 0 2 4 5]
 [0 4 2 9 0 5 0 3 1]
 [0 1 5 4 0 2 0 8 0]
 [9 0 8 0 3 7 5 0 4]]
```

## solve the sudoku puzzle
```python
# solve the sudoku puzzle and test it.
puzzle.solver()
ans = puzzle.board
print(ans)
print(equal(ans, realans).all())

[[6 3 9 2 5 8 4 1 7]
 [4 5 7 3 1 9 8 6 2]
 [2 8 1 7 4 6 9 5 3]
 [5 9 3 6 2 4 1 7 8]
 [8 2 4 5 7 1 3 9 6]
 [1 7 6 8 9 3 2 4 5]
 [7 4 2 9 8 5 6 3 1]
 [3 1 5 4 6 2 7 8 9]
 [9 6 8 1 3 7 5 2 4]]
True
```

## create m x n sudoku puzzle.
```python
puzzlemn = Sudoku(3, 4)
ans = puzzlemn.board
print(ans)
puzzlemn.generator()
mnarray = puzzlemn.board
print()
print(mnarray)

[[10  9  2  4  1  7  8  6  5 11  3 12]
 [ 5  6  1  7  3  9 11 12  8  2  4 10]
 [11 12  3  8  4  5  2 10  6  9  7  1]
 [ 6  8 12 10  2  4  7 11  9  1  5  3]
 [ 4  3  5  1  8  6 10  9  2 12 11  7]
 [ 9 11  7  2 12  3  5  1  4  8 10  6]
 [ 7  5 11  6 10  2  3  8 12  4  1  9]
 [ 1 10  4  3  6 12  9  5 11  7  8  2]
 [12  2  8  9  7 11  1  4  3 10  6  5]
 [ 3  4 10 11  9  1  6  2  7  5 12  8]
 [ 8  7  9 12  5 10  4  3  1  6  2 11]
 [ 2  1  6  5 11  8 12  7 10  3  9  4]]

[[10  0  0  0  0  7  0  0  0  0  3 12]
 [ 5  0  1  7  0  9  0  0  8  2  0  0]
 [11  0  0  0  0  5  0  0  0  9  7  1]
 [ 0  8  0 10  0  4  7  0  9  0  5  0]
 [ 0  3  0  0  8  6 10  0  0  0 11  7]
 [ 9  0  0  2  0  3  0  1  4  8  0  6]
 [ 7  5 11  0 10  2  3  8  0  4  1  0]
 [ 0 10  0  3  0 12  9  5 11  0  8  2]
 [12  2  8  9  7  0  1  0  3  0  6  0]
 [ 0  0 10 11  0  1  0  0  0  0  0  8]
 [ 8  7  0 12  5  0  4  3  0  0  0  0]
 [ 2  0  0  0  0  8 12  7  0  0  0  4]]


```

## import from the board
```python
board = [[0, 3, 9, 2, 5, 8, 4, 1, 7],
         [4, 5, 7, 3, 1, 9, 8, 6, 2],
         [2, 8, 1, 7, 4, 6, 9, 5, 3],
         [5, 9, 3, 6, 2, 4, 0, 7, 8],
         [8, 2, 4, 5, 7, 1, 3, 9, 6],
         [1, 7, 0, 8, 0, 3, 2, 4, 5],
         [7, 4, 2, 9, 8, 5, 6, 3, 1],
         [3, 1, 5, 4, 6, 2, 7, 8, 9],
         [9, 6, 8, 1, 3, 7, 5, 2, 4]]
# default sudoku size if 9*9 with width=3 height=3
# if you import from the board you must set the right width and height
puzzle = Sudoku(3, 3, board=np.array(board, dtype=int))
    print(puzzle.board)
    if puzzle.solver():
        print(puzzle.board)

[[0 3 9 2 5 8 4 1 7]
 [4 5 7 3 1 9 8 6 2]
 [2 8 1 7 4 6 9 5 3]
 [5 9 3 6 2 4 0 7 8]
 [8 2 4 5 7 1 3 9 6]
 [1 7 0 8 0 3 2 4 5]
 [7 4 2 9 8 5 6 3 1]
 [3 1 5 4 6 2 7 8 9]
 [9 6 8 1 3 7 5 2 4]]

[[6 3 9 2 5 8 4 1 7]
 [4 5 7 3 1 9 8 6 2]
 [2 8 1 7 4 6 9 5 3]
 [5 9 3 6 2 4 1 7 8]
 [8 2 4 5 7 1 3 9 6]
 [1 7 6 8 9 3 2 4 5]
 [7 4 2 9 8 5 6 3 1]
 [3 1 5 4 6 2 7 8 9]
 [9 6 8 1 3 7 5 2 4]]
```

## unsolvable sudoku puzzle
```python
board = [[0, 0, 7, 0, 4, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 8, 0, 0, 6],
         [0, 4, 1, 0, 0, 0, 9, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 7, 0],
         [0, 0, 0, 0, 0, 6, 0, 0, 0],
         [0, 0, 8, 7, 0, 0, 2, 0, 0],
         [3, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 2, 0, 0, 0, 0],
         [8, 6, 0, 0, 7, 6, 0, 0, 5]]
unsolvable = Sudoku(3, 3, board=np.array(board, dtype=int))
    print(unsolvable.board)
    if unsolvable.solver():
        print(unsolvable.board)

[[0 0 7 0 4 0 0 0 0]
 [0 0 0 0 0 8 0 0 6]
 [0 4 1 0 0 0 9 0 0]
 [0 0 0 0 0 0 1 7 0]
 [0 0 0 0 0 6 0 0 0]
 [0 0 8 7 0 0 2 0 0]
 [3 0 0 0 0 0 0 0 0]
 [0 0 0 1 2 0 0 0 0]
 [8 6 0 0 7 6 0 0 5]]
UnsolvableSudoku

```
# ToDoList
1. show the sudoku __repr__ or __str__ instead of printing puzzle.board()
2. unsolvable exception


# Bugs
If you find any bugs or errors please send me an email by: ronnie.lee@foxmail.com
