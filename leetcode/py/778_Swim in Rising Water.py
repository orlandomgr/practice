import heapq
from typing import List
from myUtils.Utils import printResult
from functools import cache


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        n = len(grid)
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = set((0, 0))

        # left, up, right, down
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        while heap:
            current, row, col = heapq.heappop(heap)
            if row == n - 1 and col == n - 1:
                return current

            for dirR, dirC in directions:
                x, y = row + dirR, col + dirC
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    heapq.heappush(heap, (max(current, grid[x][y]), x, y))
                    visited.add((x, y))


obj = Solution()

# [10, 12,  4,  6],
# [ 9, 11,  3,  5],
# [ 1,  7, 13,  8],
# [ 2,  0, 15, 14]

grid = [[10, 12, 4, 6], [9, 11, 3, 5], [1, 7, 13, 8], [2, 0, 15, 14]]
expected = 14
result = obj.swimInWater(grid)
printResult(result, expected)

grid = [[0, 2], [1, 3]]
expected = 3
result = obj.swimInWater(grid)
printResult(result, expected)

grid = [
    [0, 1, 2, 3, 4],
    [24, 23, 22, 21, 5],
    [12, 13, 14, 15, 16],
    [11, 17, 18, 19, 20],
    [10, 9, 8, 7, 6],
]
expected = 16
result = obj.swimInWater(grid)
printResult(result, expected)

grid = [[1]]
expected = 1
result = obj.swimInWater(grid)
printResult(result, expected)

grid = []
expected = 0
result = obj.swimInWater(grid)
printResult(result, expected)
