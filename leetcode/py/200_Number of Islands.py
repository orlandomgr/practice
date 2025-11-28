from typing import List
from myUtils.Utils import printResult
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rowN = len(grid)
        colN = len(grid[0])

        def visitN(r: int, c: int):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                # print(queue)
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rowN and 0 <= c < colN and grid[r][c] == "1" and (r, c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # print("r: %s c: %s val: %s" %(r, c, grid[r][c]))
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    visitN(r, c)
        return count


obj = Solution()

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
expected = 1
result = obj.numIslands(grid)
printResult(result, expected)

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
expected = 3
result = obj.numIslands(grid)
printResult(result, expected)
