from typing import List
from myUtils.Utils import printResult
from collections import deque
"""
You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), 
find the path with the maximum non-negative product. 
The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. 
If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.
"""
class Solution:    

    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        rows = len(grid)
        cols = len(grid[0])

        max_prod = [[None] * cols for _ in range(rows)]
        min_prod = [[None] * cols for _ in range(rows)]

        max_prod[0][0] = grid[0][0]
        min_prod[0][0] = grid[0][0]

        q = deque([(0, 0)])
        dirs = [(0, 1), (1, 0)]

        while q:
            r, c = q.popleft()
            cur_max = max_prod[r][c]
            cur_min = min_prod[r][c]

            for dirR, dirC in dirs:
                nr, nc = r + dirR, c + dirC
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                value = grid[nr][nc]
                candidates = [cur_max * value, cur_min * value]

                next_max = max(candidates)
                next_min = min(candidates)

                updated = False
                if max_prod[nr][nc] is None or next_max > max_prod[nr][nc]:
                    max_prod[nr][nc] = next_max
                    updated = True
                if min_prod[nr][nc] is None or next_min < min_prod[nr][nc]:
                    min_prod[nr][nc] = next_min
                    updated = True

                if updated:
                    q.append((nr, nc))

        final_max = max_prod[rows - 1][cols - 1]
        if final_max is None or final_max < 0:
            return -1
        return final_max % mod
   

obj = Solution()

grid = [[3]]
expected = 3
result = obj.maxProductPath(grid)
printResult(result, expected)

grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
expected = -1
result = obj.maxProductPath(grid)
printResult(result, expected)

grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
expected = 8
result = obj.maxProductPath(grid)
printResult(result, expected)

grid = [[1,3],[0,-4]]
expected = 0
result = obj.maxProductPath(grid)
printResult(result, expected)

