from typing import List
from myUtils.Utils import printResult

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        best = nums[0]

        for i in nums[1:]:
            current = max(i, current + i)
            best = max(best, current)

        return best


obj = Solution()

nums = [-1, -2]
expected = -1
result = obj.maxSubArray(nums)
printResult(result, expected)

nums = [-2, -1]
expected = -1
result = obj.maxSubArray(nums)
printResult(result, expected)

nums = [-2, -3, -1]
expected = -1
result = obj.maxSubArray(nums)
printResult(result, expected)

nums = [-2, -1]
expected = -1
result = obj.maxSubArray(nums)
printResult(result, expected)

nums = [-2, 1]
expected = 1
result = obj.maxSubArray(nums)
printResult(result, expected)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
expected = 6  #  [4,-1,2,1]
result = obj.maxSubArray(nums)
printResult(result, expected)

nums = [1]
expected = 1
result = obj.maxSubArray(nums)
printResult(result, expected)

nums = [5, 4, -1, 7, 8]
expected = 23  # [5, 4, -1, 7, 8]
result = obj.maxSubArray(nums)
printResult(result, expected)
