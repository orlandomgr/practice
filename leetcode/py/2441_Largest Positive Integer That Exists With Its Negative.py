from typing import List
from myUtils.Utils import printResult

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for n in nums:
            if -n in nums:
                return n
        return -1
    
obj = Solution()

nums = [-1,2,-3,3]
expected = 3
result = obj.findMaxK(nums)
printResult(result, expected)

nums = [-1,10,6,7,-7,1]
expected = 7
result = obj.findMaxK(nums)
printResult(result, expected)

nums = [-10,8,6,7,-2,-3]
expected = -1
result = obj.findMaxK(nums)
printResult(result, expected)

