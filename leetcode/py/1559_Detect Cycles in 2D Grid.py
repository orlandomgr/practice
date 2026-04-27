from myUtils.Utils import printResult
from typing import List
from collections import deque

"""
Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.
"""
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                if not visited[r][c]:
                    char = grid[r][c]
                    queue = deque([(r, c, -1, -1)])
                    visited[r][c] = True
                    
                    while queue:
                        curr_r, curr_c, pr, pc = queue.popleft()
                        # print(queue)
                        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == char:
                                if not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    queue.append((nr, nc, curr_r, curr_c))
                                elif (nr, nc) != (pr, pc):
                                    return True
        return False
    
obj = Solution()

grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
expected = True
result = obj.containsCycle(grid)
printResult(result, expected)

grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
expected = True
result = obj.containsCycle(grid)
printResult(result, expected)

grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
expected = False
result = obj.containsCycle(grid)
printResult(result, expected)
