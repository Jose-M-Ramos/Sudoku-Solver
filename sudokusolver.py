import itertools
import random

def generate_sudoku_grid():
    """Generates a 9x9 Sudoku grid with a random number of empty cells.
    Returns the generated grid as a 2D list.
    """
    grid = [[random.randint(1, 9) for _ in range(9)] for _ in range(9)]

    # make some of the cells empty
    num_empty_cells = random.randint(30, 50)
    for _ in range(num_empty_cells):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        grid[row][col] = 0

    return grid

def is_valid(grid, val, row, col):
    """Checks if the given value can be placed in the specified cell of the grid.
    Returns True if the value is valid, False otherwise.
    """
    # check the row
    if val in grid[row]:
        return False

    # check the column
    if val in (grid[i][col] for i in range(9)):
        return False

    # check the square
    square_row_start = (row // 3) * 3
    square_col_start = (col // 3) * 3

    if val in (grid[r][c] for r, c in itertools.product(range(square_row_start, square_row_start + 3), range(square_col_start, square_col_start + 3))):
        return False

    return True

def solve(grid):
    """Solves the given Sudoku puzzle using a recursive approach.
    Returns True if a solution exists, False otherwise.
    Modifies the grid to contain the solution if one exists.
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for val in range(1, 10):
                    if is_valid(grid, val, row, col):
                        grid[row][col] = val
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True
