from typing import List
from myUtils.Utils import printResult

"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid

            if nums[left] <= mid_value:
                if nums[left] <= target < mid_value:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if mid_value < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


obj = Solution()

nums = [4,5,6,7,0,1,2]
target = 0
expected = 4
result = obj.search(nums, target)
printResult(result, expected)

nums = [4,5,6,7,0,1,2]
target = 3
expected = -1
result = obj.search(nums, target)
printResult(result, expected)

nums = [1]
target = 0
expected = -1
result = obj.search(nums, target)
printResult(result, expected)
