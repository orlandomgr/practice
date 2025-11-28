from myUtils.Utils import printResult
from typing import List
from collections import deque

class Solution:
    def navigate(self, grid: List[List[int]], r:int, c:int, visited:set):
        n = len(grid)
        m = len(grid[0])
        q = deque([(r,c)])
        visited.add((r,c))
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # left, right, up, down
        isClosed = True

        while q:
            # print(q)
            r,c = q.popleft()
            for dirR, dirC in directions:
                R, C = r + dirR, c + dirC

                if R < 0 or R >= n or C < 0 or C >= m:
                    isClosed = False
                elif grid[R][C] == 0 and (R,C) not in visited:
                    q.append((R,C))
                    visited.add((R,C))

        return isClosed
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        result = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0 and (r,c) not in visited and self.navigate(grid, r,c, visited):
                    result += 1
        return result


obj = Solution()

grid = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0],
]
expected = 2
result = obj.closedIsland(grid)
printResult(result, expected)

grid = [
    [0, 0, 1, 0, 0], 
    [0, 1, 0, 1, 0], 
    [0, 1, 1, 1, 0]
    ]
expected = 1
result = obj.closedIsland(grid)
printResult(result, expected)

grid = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
]
expected = 2
result = obj.closedIsland(grid)
printResult(result, expected)
