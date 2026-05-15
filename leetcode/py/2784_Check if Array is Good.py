from typing import List
from myUtils.Utils import printResult

"""
You are given an integer array nums. We consider an array good if it is a permutation of an array base[n].

base[n] = [1, 2, ..., n - 1, n, n] (in other words, it is an array of length n + 1 which contains 1 to n - 1 exactly once, plus two occurrences of n). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

Return true if the given array is good, otherwise return false.

Note: A permutation of integers represents an arrangement of these numbers.
"""

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        maxN = nums[-1]
        n = len(nums)

        if n != maxN + 1:
            return False
        
        def is_consecutive(nums):
            if not nums: return True
            return max(nums) - min(nums) + 1 == len(nums) == len(set(nums))

        if nums[-1] != nums[-2]:
            return False
        
        nums = nums[:-1]
        return is_consecutive(nums)     
    
obj = Solution()

nums = [2, 1, 3]
expected = False
result = obj.isGood(nums)
printResult(result, expected)

nums = [1, 3, 3, 2]
expected = True
result = obj.isGood(nums)
printResult(result, expected)

nums = [1, 1]
expected = True
result = obj.isGood(nums)
printResult(result, expected)

nums = [3, 4, 4, 1, 2, 1]
expected = False
result = obj.isGood(nums)
printResult(result, expected)
