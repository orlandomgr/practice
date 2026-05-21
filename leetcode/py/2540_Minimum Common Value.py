from typing import List
from myUtils.Utils import printResult

"""
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
"""
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        common = list(set(nums1) & set(nums2))
        common.sort()
        return -1 if len(common) < 1 else common[0]

obj = Solution()

nums1 = [1,2,3]
nums2 = [2,4]
expected = 2
result = obj.getCommon(nums1, nums2)
printResult(result, expected)

nums1 = [1,2,3,6]
nums2 = [2,3,4,5]
expected = 2
result = obj.getCommon(nums1, nums2)
printResult(result, expected)
