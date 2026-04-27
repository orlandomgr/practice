from myUtils.Utils import printResult
from typing import List
from collections import deque

"""
You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.
"""
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        directions = (
            (),
            ((0, -1), (0, 1)),   # 1: left, right
            ((-1, 0), (1, 0)),   # 2: up, down
            ((0, -1), (1, 0)),   # 3: left, down
            ((0, 1), (1, 0)),    # 4: right, down
            ((0, -1), (-1, 0)),  # 5: left, up
            ((0, 1), (-1, 0))    # 6: right, up
        )
        
        queue = deque([(0, 0)])
        visited = {(0, 0)}
        
        while queue:
            r, c = queue.popleft()
            if r == n - 1 and c == m - 1:
                return True
                
            for dr, dc in directions[grid[r][c]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                    # Check if the next cell connects back
                    if (-dr, -dc) in directions[grid[nr][nc]]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        
        return False
    
obj = Solution()

grid = [
    [2,4,3],
    [6,5,2]
]
expected = True
result = obj.hasValidPath(grid)
printResult(result, expected)

grid = [[1,2,1],[1,2,1]]
expected = False
result = obj.hasValidPath(grid)
printResult(result, expected)

grid = [[1,1,2]]
expected = False
result = obj.hasValidPath(grid)
printResult(result, expected)

