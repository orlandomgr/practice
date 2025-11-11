from typing import List
from myUtils.Utils import printResult
from functools import cache
from collections import Counter
import queue
import math


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        prev = 0
        count = 1
        maxSubArrays = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
              count += 1
            else:
              maxSubArrays = max(maxSubArrays, count // 2, min(prev, count))
              prev = count
              count = 1
        maxSubArrays = max(maxSubArrays, count // 2, min(prev, count))
        return maxSubArrays


obj = Solution()

# nums = [-1, 0, 3, -5]
# expected = 1
# result = obj.maxIncreasingSubarrays(nums)
# printResult(result, expected)

# nums = [-3, -19, -8, -16]
# expected = 1
# result = obj.maxIncreasingSubarrays(nums)
# printResult(result, expected)

nums = [2, 5, 7, 8, 9, 2, 3, 4, 3, 1]
expected = 3
result = obj.maxIncreasingSubarrays(nums)
printResult(result, expected)

nums = [1, 2, 3, 4, 4, 4, 4, 5, 6, 7]
expected = 2
result = obj.maxIncreasingSubarrays(nums)
printResult(result, expected)

nums = [2,5,7,8,9,2,3,4,3,1]
expected = 3
result = obj.maxIncreasingSubarrays(nums)
printResult(result, expected)
