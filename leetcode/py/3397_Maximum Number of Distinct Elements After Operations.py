from typing import List
from myUtils.Utils import printResult
from functools import cache
from collections import Counter
import queue


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        counter = 0
        prev = -(10**10)
        for num in nums:
            current = max(num - k, prev + 1)
            if current <= num + k:
                counter += 1
                prev = current
        return counter


obj = Solution()

nums = [1, 2, 2, 3, 3, 4]
k = 2
expected = 6
result = obj.maxDistinctElements(nums, k)
printResult(result, expected)

nums = [4, 4, 4, 4]
k = 1
expected = 3
result = obj.maxDistinctElements(nums, k)
printResult(result, expected)
