# Sudoku-Solver
This code is a solution to the popular puzzle game Sudoku. The function solve() takes in a 9x9 grid representing a Sudoku puzzle and returns True if a solution exists, False otherwise. If a solution exists, the function will also modify the input grid to contain the solution.
## Requirements
This code was written and tested in Python 3.8. It should work with other versions of Python 3 as well.
This code has no external dependencies.
## How to use?
To use the solver, you will need to pass in a 9x9 grid containing the initial puzzle as a 2D list. Empty cells should be represented as -1.

```python
  from sudoku_solver import solve

  grid = [[5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]]

  solve(grid)

  print(grid)
  ```
## Explanation
The solve() function uses an iterative approach to solve the Sudoku puzzle. It keeps track of the current cell being considered using a stack, and backtracks to try new values when it reaches a dead end. The is_valid() function is used to check if a given value is valid for the current cell, considering the contents of the current row, column, and 3x3 square.

## Limitations
This solver uses an iterative approach and does not utilize any advanced techniques such as constraint propagation or search tree pruning. As a result, it may not be as efficient as more advanced solvers. However, it should be sufficient for most Sudoku puzzles.

## Future improvem
