from typing import List
from myUtils.Utils import printResult

"""
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contain:

grid[0][0]
an equal frequency of 'X' and 'Y'.
at least one 'X'.
"""
class Solution:    

    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        sumX = [0] * cols
        sumY = [0] * cols
        result = 0

        for r in range(rows):
            currX = 0
            currY = 0
            for c in range(cols):
                if grid[r][c] == 'X':
                    currX += 1
                elif grid[r][c] == 'Y':
                    currY += 1
                
                sumX[c] += currX
                sumY[c] += currY
                
                if sumX[c] > 0 and sumX[c] == sumY[c]:
                    result += 1

        return result


obj = Solution()

grid = [[".","X"],[".","Y"]]
expected = 1
result = obj.numberOfSubmatrices(grid)
printResult(result, expected)

grid = [["X","Y","."],["Y",".","."]]
expected = 3
result = obj.numberOfSubmatrices(grid)
printResult(result, expected)

grid = [["X","X"],["X","Y"]]
expected = 0
result = obj.numberOfSubmatrices(grid)
printResult(result, expected)

grid = [[".","."],[".","."]]
expected = 0
result = obj.numberOfSubmatrices(grid)
printResult(result, expected)

