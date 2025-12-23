from typing import List
from myUtils.Utils import printResult

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        res = 0
        totalOdd = sum(nums[1::2])
        totalEven = sum(nums[0::2])
        leftOdd = 0
        leftEven = 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                totalEven -= num
            else:
                totalOdd -= num

            currentEvenSum = leftEven + totalOdd
            currentOddSum = leftOdd + totalEven

            if currentEvenSum == currentOddSum:
                res += 1

            if i % 2 == 0:
                leftEven += num
            else:
                leftOdd += num
        return res
    
obj = Solution()

nums = [2,1,6,4]
expected = 1
result = obj.waysToMakeFair(nums)
printResult(result, expected)
 
nums = [1,1,1]
expected = 3
result = obj.waysToMakeFair(nums)
printResult(result, expected)

nums = [1,2,3]
expected = 0
result = obj.waysToMakeFair(nums)
printResult(result, expected)
  