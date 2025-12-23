from typing import List
from myUtils.Utils import printResult
from collections import deque

class Solution:
    def navigate(self, r, c, grid: List[List[int]], visited: set, size: int) -> int:
        q = deque()
        q.append((r,c))
        while q:
            r, c = q.popleft()
            visited.add((r,c))
            if grid[r][c] == 1:
                size +=1 
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0), ] # right, down, left, up
            for dirR, dirC in directions:
                R = r + dirR
                C = c + dirC
                if 0 <= R < self.rows and 0 <= C < self.cols and (R,C) not in visited and grid[R][C] == 1:
                    visited.add((R, C))
                    q.append((R, C))

        # print("navigate r: %s c: %s size: %s" %(r,c,size))
        return size
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        self.rows = len(grid)
        self.cols = len(grid[0])
        visited = set()
        maxArea = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    # print("grid r: %s c: %s" %(r,c))
                    currentArea = self.navigate(r, c, grid, visited, 0)
                    # print(currentArea)
                    maxArea = max(maxArea, currentArea)
        return maxArea

obj = Solution()

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
expected = 6
result = obj.maxAreaOfIsland(grid)
printResult(result, expected)

grid = [[0,0,0,0,0,0,0,0]]
expected = 0
result = obj.maxAreaOfIsland(grid)
printResult(result, expected)
