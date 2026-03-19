from typing import List
from myUtils.Utils import printResult

"""
You are given a 0-indexed integer matrix grid and an integer k.

Return the number of submatrices that contain the top-left element of the grid, 
and have a sum less than or equal to k.
"""
class Solution:    

    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        if rows < 0 or cols < 0:
            return 0
        if grid[0][0] > k:
            return 0
        
        prefix = [[0 for _ in range(cols)] for _ in range(rows)]
        prefix[0][0] = grid[0][0]
        for c in range(1, cols):
            prefix[0][c] = prefix[0][c-1] + grid[0][c]

        for r in range(1, rows):
            prefix[r][0] = prefix[r-1][0] + grid[r][0]

        for r in range(1, rows):
            for c in range(1, cols):
                prefix[r][c] = prefix[r-1][c] + prefix[r][c-1] - prefix[r-1][c-1] + grid[r][c]

        result = 0

        for r in range(rows):
            for c in range(cols):
                if prefix[r][c] <= k:
                    result += 1

        return result


obj = Solution()

grid = [[7,6,3],[6,6,1]]
k = 6
expected = 0
result = obj.countSubmatrices(grid, k)
printResult(result, expected)

grid = [[7,6,3],[6,6,1]]
k = 18
expected = 4
result = obj.countSubmatrices(grid, k)
printResult(result, expected)

grid = [[7,2,9],[1,5,0],[2,6,6]]
k = 20
expected = 6
result = obj.countSubmatrices(grid, k)
printResult(result, expected)
