from typing import List
from myUtils.Utils import printResult


class Solution:
    def swap(self, nums: List[int], idx1, idx2) -> None:
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx1 = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx1 = i
                break
        if idx1 == -1:
            for i in range(n // 2):
                self.swap(nums, i, n - 1 - i)
        else:
            for i in range(n - 1, i > idx1, -1):
                if nums[i] > nums[idx1]:
                    self.swap(nums, i, idx1)
                    break
            nums[idx1 + 1:] = nums[idx1 + 1 :][::-1]
        return nums


obj = Solution()
nums = [1, 2]
expected = [2, 1]
result = obj.nextPermutation(nums)
printResult(result, expected)

nums = [1, 2, 3]
expected = [1, 3, 2]
result = obj.nextPermutation(nums)
printResult(result, expected)

nums = [3, 2, 1]
expected = [1, 2, 3]
result = obj.nextPermutation(nums)
printResult(result, expected)

nums = [1, 1, 5]
expected = [1, 5, 1]
result = obj.nextPermutation(nums)
printResult(result, expected)
