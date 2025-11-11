from typing import List
from myUtils.Utils import printResult

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        size = len(nums)
        maxSum = -100 ** 100
        for i in range(size):
            known = {}
            numI = nums[i]
            currentSum = numI
            known[numI] = True
            for j in range(i + 1, size):
                numJ = nums[j]
                if numJ in known:
                    continue    
                if numJ < 0:
                    continue
                known[numJ] = True
                currentSum += numJ
            # print(currentSum)
            maxSum = max(maxSum, currentSum)
        
        return maxSum
        # array = [1,2,-1,-2,1,0,-1]
        # print(array)
        # array = list(set(array))
        # print(array)

obj = Solution()

nums = [-17, -15]
expected = -15
result = obj.maxSum(nums)
printResult(result, expected)

nums = [-100]
expected = -100
result = obj.maxSum(nums)
printResult(result, expected)

nums = [1,2,3,4,5]
expected = 15
result = obj.maxSum(nums)
printResult(result, expected)

nums = [1,1,0,1,1]
expected = 1
result = obj.maxSum(nums)
printResult(result, expected)

nums = [1,2,-1,-2,1,0,-1]
expected = 3
result = obj.maxSum(nums)
printResult(result, expected)