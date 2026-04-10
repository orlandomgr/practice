#!/bin/python3

from myUtils.Utils import printResult

#
# Complete the 'canPlaceSecurityCameras' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER N
#  2. 2D_INTEGER_ARRAY grid
#
def canPlaceSecurityCameras(N, grid):
    cols = set()
    diag_used = set()
    anti_diag_used = set()

    def backtrack(row):
        if row == len(grid):
            return True
        for col in range(len(grid)):
            if (
                grid[row][col] == 1
                or col in cols
                or (row + col) in diag_used
                or (row - col) in anti_diag_used
            ):
                continue
            cols.add(col)
            diag_used.add(row + col)
            anti_diag_used.add(row - col)
            if backtrack(row + 1):
                return True
            cols.remove(col)
            diag_used.remove(row + col)
            anti_diag_used.remove(row - col)
        return False

    return backtrack(0)

N = 4
grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
expected = True
result = canPlaceSecurityCameras(N, grid)
printResult(result, expected)

N = 4
grid = [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]
expected = True
result = canPlaceSecurityCameras(N, grid)
printResult(result, expected)

N = 2
grid = [[0, 1], [1, 0]]
expected = False
result = canPlaceSecurityCameras(N, grid)
printResult(result, expected)
