from typing import List
from myUtils.Utils import printResult
import heapq
import math
from itertools import combinations
import heapq
from collections import deque


class Solution:

    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right left up down

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            grid[r][c] = 2
            q.append((r, c))
            visited.add((r, c))
            for dirR,dirC in self.dirs:
                newR = r + dirR
                newC = c + dirC
                dfs(newR, newC)

        found = False
        for r in range(rows):
            if found:
                break
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        distance = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dirR,dirC in self.dirs:
                    newR = row + dirR
                    newC = col + dirC

                    if 0 <= newR < rows and 0 <= newC < cols and (newR,newC) not in visited:
                        if grid[newR][newC] == 1:
                            return distance

                        q.append((newR,newC))
                        visited.add((newR,newC))

            distance += 1

        return distance


obj = Solution()

grid = [
    [0, 1], 
    [1, 0]
]
expected = 1
result = obj.shortestBridge(grid)
printResult(result, expected)

grid = [
    [0, 1, 0], 
    [0, 0, 0], 
    [0, 0, 1]
]
expected = 2
result = obj.shortestBridge(grid)
printResult(result, expected)

grid = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
expected = 1
result = obj.shortestBridge(grid)
printResult(result, expected)
