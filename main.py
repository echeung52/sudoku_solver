import numpy as np

grid = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]]


#checks if a number is able to be inserted into a certain spot
def valid(grid, row, col, target):
    for i in range(9):
        if grid[row][i] == target:
            return False

    for i in range(9):
        if grid[i][col] == target:
            return False
    
    x = row - row % 3
    y = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[x+i][y+j] == target:
                return False

    return True
    
def solve(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if valid(grid, i, j, n):
                        grid[i][j] = n
                        solve(grid)
                        grid[i][j] = 0

                return
    print(np.matrix(grid))
    input("Press enter for more possible solutions")

solve(grid)
print("There are no more possible solutions")
    
