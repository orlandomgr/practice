from typing import List
from myUtils.Utils import printResult
from functools import cache


class Solution:

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m = len(heights)
        n = len(heights[0])
        # left, up, right, down
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def checkCell(row, col, visited):
            visited.add((row, col))
            for dirX, dirY in directions:
                x, y = row + dirX, col + dirY
                if 0 <= x < m and 0 <= y < n:
                    if (x, y) not in visited:
                        if heights[x][y] >= heights[row][col]:
                            checkCell(x, y, visited)

        pacific = set()
        atlantic = set()

        for j in range(n):
            checkCell(0, j, pacific)
        for i in range(m):
            checkCell(i, 0, pacific)

        for j in range(n):
            checkCell(m - 1, j, atlantic)
        for i in range(m):
            checkCell(i, n - 1, atlantic)
        
        result = []
        combined = list(pacific & atlantic)
        combined.sort()
        for x,y in combined:
            result.append([x,y])
        return result

    
obj = Solution()

heights = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
expected = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
result = obj.pacificAtlantic(heights)
printResult(result, expected)

heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4],
]
expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
result = obj.pacificAtlantic(heights)
printResult(result, expected)

heights = [[1]]
expected = [[0, 0]]
result = obj.pacificAtlantic(heights)
printResult(result, expected)

# [1,2,3],
# [8,9,4],
# [7,6,5]
