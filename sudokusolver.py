import itertools

def solve_sudoku(grid):
    """Solves the given Sudoku puzzle and returns the solution as a 2D list.
    If the puzzle has multiple solutions or is unsolvable, returns None.
    """
    def find_empty_cell(grid):
        """Finds the first empty cell in the grid.
        Returns a tuple (row, col) representing the cell's position, or None if no empty cells were found.
        """
        for row, col in itertools.product(range(9), range(9)):
            if grid[row][col] == 0:
                return (row, col)
        return None

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
        Returns True if a solution was found, False otherwise.
        Modifies the grid to contain the solution.
        """
        empty_cell = find_empty_cell(grid)
        if empty_cell is None:
            # no more empty cells, puzzle is solved
            return True

        row, col = empty_cell

        # try filling in the empty cell with a valid value
        for val in range(1, 10):
            if is_valid(grid, val, row, col):
                grid[row][col] = val
                if solve(grid):
                    # solution was found
                    return True
                grid[row][col] = 0
        # no valid value was found, puzzle is unsolvable
        return False

    if solve(grid):
        return grid
    else:
        return None

