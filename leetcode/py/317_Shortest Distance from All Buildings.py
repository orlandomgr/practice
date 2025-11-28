from typing import List
from myUtils.Utils import printResult
from collections import deque

class Solution:
    def getStartingPoints(self, grid: List[List[int]]):
        n = len(grid)
        m = len(grid[0])
        buildings = []
        positions = []
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    buildings.append((r,c,0))
                    grid[r][c] = "B"
                elif grid[r][c] == 2:
                    grid[r][c] = "X"
                else:
                    positions.append((r,c,0))
        return buildings, positions


    def navigate(self, rooms: List[List[int]], r, c, cost, visited: List[List[set]], level: int):
        n = len(rooms)
        m = len(rooms[0])
        q = deque()
        q.append((r, c, cost))
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # left, right, up, down
        while q:
            r,c,cost = q.popleft()
            if level in visited[r][c]:
                continue
            if type(grid[r][c]) is int:
                rooms[r][c] += cost
                visited[r][c].add(level)
            for dirR, dirC in directions:
                R, C = r + dirR, c + dirC
                if 0 <= R < n and 0 <= C < m and rooms[R][C] != "B" and rooms[R][C] != "X" and level not in visited[R][C]:
                    q.append((R,C,cost+1))

    def shortestDistance(self, grid: List[List[int]]) -> int:
        """
        Do not return anything, modify grid in-place instead.
        """
        n = len(grid)
        m = len(grid[0])
        visited = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(set())
            visited.append(row)

        # print(grid)
        buildings, positions = self.getStartingPoints(grid)
        if len(positions) < 1:
            return -1
        
        level = 0
        for r,c,cost in buildings:
            level += 1
            self.navigate(grid, r,c, cost, visited, level)

        minPath = 10**10
        for r in range(n):
            for c in range(m):
                if type(grid[r][c]) is not int or len(visited[r][c]) != level:
                    continue 
                minPath = min(minPath, grid[r][c])

        return minPath if minPath != 10**10 else -1

obj = Solution()

grid = [[0,2,1],[1,0,2],[0,1,0]]
expected = -1
result = obj.shortestDistance(grid)
printResult(result, expected)

grid = [[1,2,0]]
expected = -1
result = obj.shortestDistance(grid)
printResult(result, expected)

grid = [[1,0,2,0,1], [0,0,0,0,0], [0, 0,1,0,0]]
expected = 7
result = obj.shortestDistance(grid)
printResult(result, expected)

grid = [[1,0]]
expected = 1
result = obj.shortestDistance(grid)
printResult(result, expected)

grid = [[1]]
expected = -1
result = obj.shortestDistance(grid)
printResult(result, expected)
