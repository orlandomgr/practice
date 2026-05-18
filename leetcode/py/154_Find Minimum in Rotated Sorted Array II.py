from myUtils.Utils import printResult
from typing import List

"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]



obj = Solution()

nums = [1,3,5]
expected = 1
result = obj.findMin(nums)
printResult(result, expected)

nums = [2,2,2,0,1]
expected = 0
result = obj.findMin(nums)
printResult(result, expected)
