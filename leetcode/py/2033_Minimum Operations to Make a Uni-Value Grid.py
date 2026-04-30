from typing import List
from myUtils.Utils import printResult

"""
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.
"""
class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = sorted(val for row in grid for val in row)

        if len(set(v % x for v in nums)) > 1:
            return -1

        median = nums[len(nums) // 2]

        return sum(abs(v - median) // x for v in nums)


obj = Solution()

grid = [
    [2,4],
    [6,8]
]
x = 2
expected = 4
result = obj.minOperations(grid, x)
printResult(result, expected)

grid = [[1,5],[2,3]]
x = 1
expected = 5
result = obj.minOperations(grid, x)
printResult(result, expected)

grid = [[1,2],[3,4]]
x = 2
expected = -1
result = obj.minOperations(grid, x)
printResult(result, expected)

