from typing import List
from myUtils.Utils import printResult

"""
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.
"""
class Solution:    

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        total = 0

        row = [0] * rows
        col = [0] * cols

        for r in range(rows):
            for c in range(cols):
                total += grid[r][c]
                row[r] += grid[r][c]
                col[c] += grid[r][c]

        if total % 2 != 0:
            return False

        target = total // 2

        curr = 0
        for r in range(rows - 1):
            curr += row[r]
            if curr == target:
                return True

        curr = 0
        for c in range(cols - 1):
            curr += col[c]
            if curr == target:
                return True

        return False


obj = Solution()

grid = [[54756,54756]]
expected = True
result = obj.canPartitionGrid(grid)
printResult(result, expected)

grid = [[1,4],[2,3]]
expected = True
result = obj.canPartitionGrid(grid)
printResult(result, expected)

grid = [[1,3],[2,4]]
expected = False
result = obj.canPartitionGrid(grid)
printResult(result, expected)
