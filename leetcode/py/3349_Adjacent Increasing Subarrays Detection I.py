from typing import List
from myUtils.Utils import printResult
from functools import cache
from collections import Counter
import queue
import math


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        def isIncreasingArray(nums: List[int]):
            print(nums)
            m = len(nums)
            for j in range(m - 1):
                if nums[j] >= nums[j + 1]:
                    return False
            return True

        n = len(nums)
        for i in range(n - ((2 * k) - 1)):
            left = isIncreasingArray(nums[i : i + k])
            right = isIncreasingArray(nums[i + k : i + k + k])
            if left and right:
                return True
        return False


obj = Solution()

nums = [-3, -19, -8, -16]
k = 2
expected = False
result = obj.hasIncreasingSubarrays(nums, k)
printResult(result, expected)

nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
k = 3
expected = True
result = obj.hasIncreasingSubarrays(nums, k)
printResult(result, expected)

nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
k = 5
expected = False
result = obj.hasIncreasingSubarrays(nums, k)
printResult(result, expected)
