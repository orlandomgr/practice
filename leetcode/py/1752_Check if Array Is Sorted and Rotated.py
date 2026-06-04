from typing import List
from myUtils.Utils import printResult

"""
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.
"""
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        drops = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
                if drops > 1:
                    return False

        return True

obj = Solution()

nums = [3,4,5,1,2]
expected = True
result = obj.check(nums)
printResult(result, expected)

nums = [2,1,3,4]
expected = False
result = obj.check(nums)
printResult(result, expected)

nums = [1,2,3]
expected = True
result = obj.check(nums)
printResult(result, expected)

