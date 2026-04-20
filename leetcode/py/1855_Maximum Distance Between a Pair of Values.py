from typing import List
from myUtils.Utils import printResult

"""
You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.
"""

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            i += nums1[i] > nums2[j]
            j += 1 
        
        return max(0, j - i - 1)

obj = Solution()

nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]
expected = 2
result = obj.maxDistance(nums1, nums2)
printResult(result, expected)

nums1 = [2,2,2]
nums2 = [10,10,1]
expected = 1
result = obj.maxDistance(nums1, nums2)
printResult(result, expected)

nums1 = [30,29,19,5]
nums2 = [25,25,25,25,25]
expected = 2
result = obj.maxDistance(nums1, nums2)
printResult(result, expected)

