from typing import List
from myUtils.Utils import printResult
import heapq

"""
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.
"""
class Solution:    
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        indices = [i for i, x in enumerate(nums) if x == target]
        lowest = 10**10
        if start in indices:
            return 0
        for i in indices:
            lowest = min(lowest, abs(i - start))
        return lowest

obj = Solution()

nums = [1,2,3,4,5]
target = 5
start = 3
expected = 1
result = obj.getMinDistance(nums, target, start)
printResult(result, expected)

nums = [1]
target = 1
start = 0
expected = 0
result = obj.getMinDistance(nums, target, start)
printResult(result, expected)

nums = [1,1,1,1,1,1,1,1,1,1]
target = 1
start = 0
expected = 0
result = obj.getMinDistance(nums, target, start)
printResult(result, expected)
