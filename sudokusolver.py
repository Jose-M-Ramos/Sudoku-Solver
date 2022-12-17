def find_next_empty(grid):
    """Finds the next empty cell in the grid.
    Returns the row and column indices of the cell as a tuple, or (None, None) if there are no empty cells.
    """
    for i, cell in enumerate(grid):
        if cell == -1:
            return i // 9, i % 9

    return None, None

def is_valid(grid, val, row, col):
    """Checks if the given value can be placed in the specified cell of the grid.
    Returns True if the value is valid, False otherwise.
    """
    # check the row
    if val in grid[row]:
        return False

    # check the column
    for i in range(9):
        if grid[i][col] == val:
            return False

    # check the square
    square_row_start = (row // 3) * 3
    square_col_start = (col // 3) * 3

    for r in range(square_row_start, square_row_start + 3):
        for c in range(square_col_start, square_col_start + 3):
            if grid[r][c] == val:
                return False

    return True

def solve(grid):
    """Solves the given Sudoku puzzle using an iterative approach.
    Returns True if a solution exists, False otherwise.
    Modifies the grid to contain the solution if one exists.
    """
    stack = []
    row, col = find_next_empty(grid)

    while row is not None:
        for val in range(1, 10):
            # check if this is a valid value
            if is_valid(grid, val, row, col):
                # if this is a valid value, then place it in the cell
                grid[row][col] = val
                stack.append((row, col))  # add current position to the stack
                row, col = find_next_empty(grid)  # find the next empty cell
                break  # move on to the next cell
        else:  # if no valid value was found for the current cell
            # backtrack and try a new value
            grid[row][col] = -1
            row, col = stack.pop()

    return row is None  # if no empty cells were found, return True, else return False
