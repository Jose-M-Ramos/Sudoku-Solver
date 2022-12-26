# Sudoku-Solver
This code is a solution to the popular puzzle game Sudoku. The function solve_sudoku() takes in a 9x9 grid representing a Sudoku puzzle and returns the solution( it there is one), and None otherwise. 

<p align="center">
  <img src="https://github.com/Jose-M-Ramos/Sudoku-Solver/blob/main/sudoku_solver.jpg" width="800" height="400">
</p>


## Requirements
This code was written and tested in Python 3.9.5 It should work with other versions of Python 3 as well. This code requires the following Python modules:

* random: For generating random numbers.

* itertools: For generating combinations of indices.

## How to use?
Here is an example of how to use these functions to generate and solve a Sudoku puzzle:

```python
import itertools
import random

from sudokugenerator import generate_sudoku_grid
from sudokusolver import solve_sudoku

# generate a random Sudoku grid
grid = generate_sudoku_grid()

#print the generated Sudoku grid
for i in grid:
  print(i)

# solve the grid
solution = solve_sudoku(grid)

# print the solution
for row in solution:
  print(row)


  ```
## Explanation
This program contains two functions that can be used to generate and solve Sudoku puzzles.

The generate_sudoku_grid function generates a 9x9 Sudoku grid with a random number of empty cells. It uses a recursive approach to fill in the cells with random values, making sure that the values are valid according to the Sudoku rules. If a puzzle can't be generated, the function starts over with a new grid.You can also modify the generate_sudoku_grid function to generate a Sudoku grid with a specific number of empty cells by passing the desired number as an argument.

The solve_sudoku function takes a Sudoku grid as an argument and returns the solution as a 2D list. It uses a recursive approach to find a valid value for each empty cell, making sure that the values are valid according to the Sudoku rules. If the puzzle has multiple solutions or is unsolvable, the function returns None.



## Limitations
This Sudoku solver is a basic implementation and may not be able to solve all puzzles. It uses a recursive approach to try all possible values for empty cells and backtracks when it reaches a dead end. This can be computationally expensive for very difficult puzzles.

## Areas of improvement

There are several techniques that can be used to solve more difficult Sudoku puzzles, some of which are more efficient than the recursive approach used in the code provided. Here are a few examples:

* Single position: If a cell has only one possible value, it can be filled in immediately.
* Single possibility: If a certain digit can only be placed in one cell within a row, column, or block, it can be filled in immediately.
* Naked pairs/triples: If there are two or three cells in a row, column, or block that can only be filled with the same two or three digits, these digits can be eliminated from the rest of the cells in that row, column, or block.
* Hidden pairs/triples: If there are two or three digits that can only be placed in two or three cells within a row, column, or block, the other digits can be eliminated from those cells.
* Pointing pairs/triples: If there are two or three cells in a row or column that can only be filled with the same two or three digits, and these cells are in the same block, the other digits can be eliminated from the rest of the cells in that block.
* X-wing: If there are two rows or columns that have only two cells that can be filled with the same digit, and these cells are in the same block, the digit can be eliminated from the rest of the cells in that block.


By using a combination of these techniques and applying them in the appropriate order, it is possible to solve more difficult Sudoku puzzles efficiently.
