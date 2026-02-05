from typing import List
from myUtils.Utils import printResult
from collections import defaultdict, Counter, OrderedDict
import heapq
from functools import cache
import re
import math

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        i = math.inf
        j = math.inf
        for z in range(n):
            if nums[z] <= i:
                i = nums[z]
            elif nums[z] <= j:
                j = nums[z]
            else:
                return True
        return False


obj = Solution()

nums = [1, 5, 0, 4, 1, 3]
expected = True
result = obj.increasingTriplet(nums)
printResult(result, expected)

nums = [4, 5, 2147483647, 1, 2]
expected = True
result = obj.increasingTriplet(nums)
printResult(result, expected)

nums = [20, 100, 10, 12, 5, 13]
expected = True
result = obj.increasingTriplet(nums)
printResult(result, expected)

nums = [1, 2, 3, 4, 5]
expected = True
result = obj.increasingTriplet(nums)
printResult(result, expected)

nums = [5, 4, 3, 2, 1]
expected = False
result = obj.increasingTriplet(nums)
printResult(result, expected)

nums = [2, 1, 5, 0, 4, 6]
expected = True
result = obj.increasingTriplet(nums)
printResult(result, expected)
