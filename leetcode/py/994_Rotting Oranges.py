from myUtils.Utils import printResult
from typing import List
from collections import deque


class Solution:
    def count(self, grid: List[List[int]]):
        fresh = 0
        rotten = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1: # fresh
                    fresh += 1
                elif grid[r][c] == 2: # rotten
                    rotten += 1
        return (fresh, rotten)
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        q = deque([(0,0)])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # left, right, up, down
        fresh, _ = self.count(grid)
        days = 0
        while fresh > 0: 
            # print(fresh)
            # print(grid)
            q.append((0,0))
            visited = set()
            days += 1
            marked = set()
            updated = False
            while q:
                r,c = q.popleft()
                if (r,c) in visited:
                    continue
                # print("r: %s c: %s" %(r,c))

                # visited.add((r,c))
                for dirR, dirC in directions:
                    newR, newC = r + dirR, c + dirC
                    if 0 <= newR < self.rows and 0 <= newC < self.cols: # and (newR,newC) not in visited:
                        if grid[r][c] == 2 and grid[newR][newC] == 1:
                            marked.add((newR, newC))
                        q.append((newR, newC))
                visited.add((r,c))
                

            for r,c in marked:
                # print("marked r: %s c: %s" %(r,c))
                grid[r][c] = 2
                fresh -= 1
                updated = True

            if not updated and fresh > 0:
                return -1
            
        return days


obj = Solution()

grid = [[1,2]]
expected = 1
result = obj.orangesRotting(grid)
printResult(result, expected)

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
expected = 4
result = obj.orangesRotting(grid)
printResult(result, expected)

grid = [[2,1,1],[0,1,1],[1,0,1]]
expected = -1
result = obj.orangesRotting(grid)
printResult(result, expected)

grid = [[0,2]]
expected = 0
result = obj.orangesRotting(grid)
printResult(result, expected)

