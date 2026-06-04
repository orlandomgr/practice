from typing import List
from myUtils.Utils import printResult
import heapq

"""
You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.
"""

class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = 10**10

        def getSum(num: int):
            res = 0
            while num > 0:
                res += num % 10
                num //= 10
            return res
        
        for n in nums:
            result = min(result, getSum(n))
        return result

    
obj = Solution()

nums = [10,12,13,14]
expected = 1
result = obj.minElement(nums)
printResult(result, expected)

nums = [1,2,3,4]
expected = 1
result = obj.minElement(nums)
printResult(result, expected)

nums = [999,19,199]
expected = 10
result = obj.minElement(nums)
printResult(result, expected)
