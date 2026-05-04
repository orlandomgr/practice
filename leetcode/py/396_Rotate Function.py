from myUtils.Utils import printResult
from typing import List
from collections import deque

"""
You are given an integer array nums of length n.

Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
Return the maximum value of F(0), F(1), ..., F(n-1).

The test cases are generated so that the answer fits in a 32-bit integer.
"""
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        totalSum = sum(nums)

        max = curr = sum([i * val for i, val in enumerate(nums)])

        for i in range(1, n):
            curr = curr + totalSum - n * nums[n - i]
            if curr > max:
                 max = curr

        return max


obj = Solution()

nums = [4,3,2,6]
expected = 26
result = obj.maxRotateFunction(nums)
printResult(result, expected)

nums = [100]
expected = 0
result = obj.maxRotateFunction(nums)
printResult(result, expected)
