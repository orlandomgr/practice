from typing import List
from myUtils.Utils import printResult

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas -= 1
            
        return True


obj = Solution()

nums = [5,9,3,2,1,0,2,3,3,1,0,0]
expected = True
result = obj.canJump(nums)
printResult(result, expected)

nums = [3,0,8,2,0,0,1]
expected = True
result = obj.canJump(nums)
printResult(result, expected)

nums = [0,2,3]
expected = False
result = obj.canJump(nums)
printResult(result, expected)

nums = [1]
expected = True
result = obj.canJump(nums)
printResult(result, expected)

nums = [2,3,1,1,4]
expected = True
result = obj.canJump(nums)
printResult(result, expected)
            
nums = [3,2,1,0,4]
expected = False
result = obj.canJump(nums)
printResult(result, expected)
