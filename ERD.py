ROWS = 4
COLS = 3

def create_grid():
    grid = []
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(0)
        #endfor
        grid.append(row)
    #endfor
    return grid
#enddef

def print_grid(grid):
    for row in grid:
        print(row)
    #endfor
#enddef

def update_grid(grid, row, col, item):
    grid[row][col] = item
#enddef

grid = create_grid()

update_grid(grid, 2, 1, 1)
update_grid(grid, 1, 1, 1)

print_grid(grid)
