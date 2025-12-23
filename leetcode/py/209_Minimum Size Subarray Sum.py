from typing import List
from myUtils.Utils import printResult

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        
        if sum(nums) < target:
            return 0

        n = len(nums)

        i = 0
        j = 0
        result = n
        curr = nums[0]
        while j < n:
            if curr >= target:
                result = min(result, j-i+1)
                curr -= nums[i]
                i += 1
            else:
                j += 1
                if j < n:
                    curr += nums[j]

        return result
    
obj = Solution()

target = 11
nums = [1,2,3,4,5]
expected = 3
result = obj.minSubArrayLen(target, nums)
printResult(result, expected)

target = 7
nums = [2,3,1,2,4,3]
expected = 2
result = obj.minSubArrayLen(target, nums)
printResult(result, expected)

target = 4
nums = [1,4,4]
expected = 1
result = obj.minSubArrayLen(target, nums)
printResult(result, expected)

target = 11
nums = [1,1,1,1,1,1,1,1]
expected = 0
result = obj.minSubArrayLen(target, nums)
printResult(result, expected)
