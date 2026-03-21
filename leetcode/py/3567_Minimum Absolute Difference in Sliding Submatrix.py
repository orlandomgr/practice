from typing import List
from myUtils.Utils import printResult

"""
You are given an m x n integer matrix grid and an integer k.

For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.

Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.

Note: If all elements in the submatrix have the same value, the answer will be 0.

A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.
"""
class Solution:    

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        if 0 <= rows < k or 0 <= cols < k:
            return [[0]]
        
        def getMinDiff(row, col):
            arr = set()
            for r in range(row, row + k):
                for c in range(col, col + k):
                    # print(f"min row: {r} col: {c}")
                    arr.add(grid[r][c])
            # print(arr)
            arr = list(arr)
            arr.sort()

            min_diff = float('inf')                
            for i in range(len(arr) - 1):
                current_diff = abs(arr[i + 1] - arr[i])
                min_diff = min(min_diff, current_diff)
                        
            return min_diff if min_diff != float('inf') else 0

        result = []
        for r in range(0, rows - k + 1):
            res = []
            for c in range(0, cols - k + 1):
                # print(f"row: {r} col: {c}")
                res.append(getMinDiff(r, c)) 
            result.append(res)

        # print(result)

        return result
   

obj = Solution()

grid = [[1,8],[3,-2]]
k = 2
expected = [[2]]
result = obj.minAbsDiff(grid, k)
printResult(result, expected)

grid = [[3,-1]]
k = 1
expected = [[0,0]]
result = obj.minAbsDiff(grid, k)
printResult(result, expected)

grid = [
    [1,-2,3],
    [2,3,5]]
k = 2
expected = [[1,2]]
result = obj.minAbsDiff(grid, k)
printResult(result, expected)

