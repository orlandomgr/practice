from myUtils.Utils import printResult
from typing import List

class Solution:

    """
    Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

    A grid is said to be valid if all the cells above the main diagonal are zeros.

    Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

    The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).
    """  
    def getMaxRight(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        maxRight = []
        for r in range(n):
            idx = -1
            for c in range(n):
                if grid[r][c] == 1:
                    idx = c
            maxRight.append(idx)
        return maxRight
    
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxRight = self.getMaxRight(grid)

        swaps = 0
        for i in range(n):
            j = i
            while j < n and maxRight[j] > i:
                j += 1
            if j == n:
                return -1
            while j > i:
                maxRight[j], maxRight[j - 1] = maxRight[j - 1], maxRight[j]
                swaps += 1
                j -= 1
        return swaps

obj = Solution()

grid = [
    [1,0,0,0,0,0],
    [0,1,0,1,0,0],
    [1,0,0,0,0,0],
    [1,1,1,0,0,0],
    [1,1,0,1,0,0],
    [1,0,0,0,0,0]
    ]
expected = 2
result = obj.minSwaps(grid)
printResult(result, expected)

grid = [
    [0,0,1],
    [1,1,0],
    [1,0,0]
    ]
expected = 3
result = obj.minSwaps(grid)
printResult(result, expected)

grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
expected = -1
result = obj.minSwaps(grid)
printResult(result, expected)

grid = [[1,0,0],[1,1,0],[1,1,1]]
expected = 0
result = obj.minSwaps(grid)
printResult(result, expected)

