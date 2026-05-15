from myUtils.Utils import printResult
from typing import List

"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]



obj = Solution()

nums = [3,4,5,1,2]
expected = 1
result = obj.findMin(nums)
printResult(result, expected)

nums = [4,5,6,7,0,1,2]
expected = 0
result = obj.findMin(nums)
printResult(result, expected)

nums = [11,13,15,17]
expected = 11
result = obj.findMin(nums)
printResult(result, expected)
