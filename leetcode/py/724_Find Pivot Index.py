from typing import List
from myUtils.Utils import printResult

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        rSum = sum(nums[1:])
        if rSum == 0:
            return 0

        lSum = [0] * n
        rSum = [0] * n
        lS = 0
        rS = 0
        for i in range(n):
            lS += nums[i]
            rS += nums[n-1-i]

            lSum[i] = lS
            rSum[n-1-i] = rS

        # print(lSum)
        # print(rSum)


        for i in range(n-2):
            if lSum[i] == rSum[i+2]:
                return i + 1

        lSum = sum(nums[:-1])
        if lSum == 0:
            return n - 1

        # print(lSum)
        # print(rSum)

        # for i in range(len(nums)):
        #     # print(nums[i+1:])
        #     if i == 0:
        #         rSum = sum(nums[i+1:])
        #         if rSum == 0:
        #             return 0
        #     else:
        #         lSum = sum(nums[:i])
        #         rSum = sum(nums[i+1:])
        #         if lSum == rSum:
        #             return i
        return -1
    
obj = Solution()

nums = [-1,-1,1,1,0,0]
expected = 4
result = obj.pivotIndex(nums)
printResult(result, expected)

nums = [-1,-1,0,1,1,0]
expected = 5
result = obj.pivotIndex(nums)
printResult(result, expected)

nums = [1,7,3,6,5,6]
expected = 3
result = obj.pivotIndex(nums)
printResult(result, expected)

nums = [1,2,3]
expected = -1
result = obj.pivotIndex(nums)
printResult(result, expected)

nums = [2,1,-1]
expected = 0
result = obj.pivotIndex(nums)
printResult(result, expected)
