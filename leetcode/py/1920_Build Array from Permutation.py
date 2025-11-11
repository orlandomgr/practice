from typing import List
from myUtils.Utils import printResult

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result
    

obj = Solution()

nums = [0,2,1,5,3,4]
expected = [0,1,2,4,5,3]
result = obj.buildArray(nums)
printResult(result, expected)    

nums = [5,0,1,2,3,4]
expected = [4,5,0,1,2,3]
result = obj.buildArray(nums)
printResult(result, expected)    

