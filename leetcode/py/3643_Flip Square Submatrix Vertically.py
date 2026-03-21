from typing import List
from myUtils.Utils import printResult

"""
You are given an m x n integer matrix grid, and three integers x, y, and k.

The integers x and y represent the row and column indices of the top-left corner of a square submatrix and the integer k represents the size (side length) of the square submatrix.

Your task is to flip the submatrix by reversing the order of its rows vertically.

Return the updated matrix.
"""
class Solution:    

    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        if x < 0 or y < 0 or x + k > rows or y + k > cols:
            return grid
        
        # Flip vertically by reversing each column in the submatrix
        for col in range(y, y + k):
            for i in range(k // 2):
                grid[x + i][col], grid[x + k - 1 - i][col] = grid[x + k - 1 - i][col], grid[x + i][col]
        
        return grid
   

obj = Solution()

grid =  [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
x = 1
y = 0
k = 3
expected = [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]
result = obj.reverseSubmatrix(grid, x, y, k)
printResult(result, expected)

grid = [[3,4,2,3],[2,3,4,2]]
x = 0
y = 2
k = 2
expected = [[3,4,4,2],[2,3,2,3]]
result = obj.reverseSubmatrix(grid, x, y, k)
printResult(result, expected)

grid = [
    [ 6, 16, 14],
    [ 1,  2, 19],
    [14, 17, 15],
    [18,  7,  6],
    [14, 12,  5]
    ]
x = 2
y = 1
k = 2
expected = [[6,16,14],[1,2,19],[14,7,6],[18,17,15],[14,12,5]]
result = obj.reverseSubmatrix(grid, x, y, k)
printResult(result, expected)

