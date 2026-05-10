from myUtils.Utils import printResult
from typing import List

"""
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.
"""

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid or not grid[0]:
            return grid
        
        n, m = len(grid), len(grid[0])
        layers = min(n, m) // 2
        
        for layer in range(layers):
            # Define boundaries
            top, bottom = layer, n - 1 - layer
            left, right = layer, m - 1 - layer
            
            # Extract perimeter
            perimeter = []
            # Top row: left to right
            for j in range(left, right + 1):
                perimeter.append(grid[top][j])
            # Right column: top+1 to bottom
            for i in range(top + 1, bottom + 1):
                perimeter.append(grid[i][right])
            # Bottom row: right-1 to left
            for j in range(right - 1, left - 1, -1):
                perimeter.append(grid[bottom][j])
            # Left column: bottom-1 to top+1
            for i in range(bottom - 1, top, -1):
                perimeter.append(grid[i][left])
            
            # Rotate left by k % length
            length = len(perimeter)
            shift = k % length
            rotated = perimeter[shift:] + perimeter[:shift]
            
            # Put back
            idx = 0
            # Top row
            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1
            # Right column
            for i in range(top + 1, bottom + 1):
                grid[i][right] = rotated[idx]
                idx += 1
            # Bottom row
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            # Left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
        
        return grid
    
obj = Solution()

grid = [[40,10],[30,20]]
k = 1
expected = [[10,20],[40,30]]
result = obj.rotateGrid(grid, k)
printResult(result, expected)

grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
k = 2
expected = [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
result = obj.rotateGrid(grid, k)
printResult(result, expected)
