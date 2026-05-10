from typing import List
from myUtils.Utils import printResult
import math
from functools import cache

"""
You are given a 0-indexed array nums of n integers and an integer target.

You are initially positioned at index 0. In one step, you can jump from index i to any index j such that:

0 <= i < j < n
-target <= nums[j] - nums[i] <= target
Return the maximum number of jumps you can make to reach index n - 1.

If there is no way to reach index n - 1, return -1.
"""

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i : int):
            if i == n - 1:
                return 0
            res = -math.inf
            for j in range(i+1, n):
                if abs(nums[j] - nums[i]) <= target:
                    res = max(res, dfs(j) + 1)
            return res
        
        result = dfs(0)
        return -1 if result < 0 else result

obj = Solution()

nums = [1,3,6,4,1,2]
target = 2
expected = 3
result = obj.maximumJumps(nums, target)
printResult(result, expected)

nums = [1,3,6,4,1,2]
target = 3
expected = 5
result = obj.maximumJumps(nums, target)
printResult(result, expected)

nums = [1,3,6,4,1,2]
target = 0
expected = -1
result = obj.maximumJumps(nums, target)
printResult(result, expected)
