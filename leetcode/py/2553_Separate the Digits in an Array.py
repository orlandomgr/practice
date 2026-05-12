from typing import List
from myUtils.Utils import printResult

"""
Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
"""
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            tmp = []
            while n > 0:
                tmp.append(n % 10)
                n //= 10                     
            result += (tmp[::-1])
        return result


obj = Solution()

nums = [13,25,83,77]
expected = [1,3,2,5,8,3,7,7]
result = obj.separateDigits(nums)
printResult(result, expected)

nums = [7,1,3,9]
expected = [7,1,3,9]
result = obj.separateDigits(nums)
printResult(result, expected)
