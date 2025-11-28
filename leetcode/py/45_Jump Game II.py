from typing import List
from myUtils.Utils import printResult

class Solution:

    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        # print("size: %s" %(n))
        idx = n 
        jumps = 0
        while idx > 0:
            newIdx = 10**10
            for i in range(idx, -1, -1):
                if i + nums[i] >= idx:
                    newIdx = min(newIdx, i)
            jumps += 1
            idx = newIdx
        return jumps


obj = Solution()

nums = [2,3,1,1,4]
expected = 2
result = obj.jump(nums)
printResult(result, expected)

nums = [2,3,0,1,4]
expected = 2
result = obj.jump(nums)
printResult(result, expected)

nums = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
expected = 5
result = obj.jump(nums)
printResult(result, expected)

