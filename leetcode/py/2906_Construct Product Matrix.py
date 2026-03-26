from typing import List
from myUtils.Utils import printResult
"""
Given a 0-indexed 2D integer matrix grid of size n * m, we define a 0-indexed 2D matrix p of size n * m as the product matrix of grid if the following condition is met:

Each element p[i][j] is calculated as the product of all elements in grid except for the element grid[i][j]. This product is then taken modulo 12345.
Return the product matrix of grid.
"""
class Solution:    

    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        mod = 12345
        result = [[0] * cols for _ in range(rows) ]
        suffix = 1
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                result[i][j] = suffix
                suffix = (suffix * (grid[i][j] % mod)) % mod

        prefix = 1
        for i in range(rows):
            for j in range(cols):
                result[i][j] = (result[i][j] * prefix) % mod
                prefix = (prefix * (grid[i][j] % mod)) % mod

        return result
   

obj = Solution()

grid = [[1,2],[3,4]]
expected = [[24,12],[8,6]]
result = obj.constructProductMatrix(grid)
printResult(result, expected)

grid = [[12345],[2],[1]]
expected = [[2],[0],[0]]
result = obj.constructProductMatrix(grid)
printResult(result, expected)

