from typing import List
from myUtils.Utils import printResult
from functools import cache
from itertools import combinations

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        size = len(nums)
        mod = 10**9 + 7
        left = 0
        right = size - 1
        result = 0
        powers = [1] * size
        for i in range(1, size):
            powers[i] = (powers[i - 1] * 2) % mod

        while left <= right:
            if nums[left] + nums[right] <= target:
                # print("i: %s j: %s " %(nums[left],nums[right]))
                result = (result + powers[right - left]) % mod
                left += 1
            else:
                right -= 1
        return result

# mcp server 
# model contex protocol 



obj = Solution()

nums = [3,5,6,7]
target = 9
expected = 4
result = obj.numSubseq(nums, target)
printResult(result, expected)

nums = [3,3,6,8]
target = 10
expected = 6
result = obj.numSubseq(nums, target)
printResult(result, expected)

nums = [2,3,3,4,6,7]
target = 12
expected = 61
result = obj.numSubseq(nums, target)
printResult(result, expected)
