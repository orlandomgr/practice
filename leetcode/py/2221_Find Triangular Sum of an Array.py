from typing import List
from myUtils.Utils import printResult
from functools import cache
import heapq

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        
        array = []
        for i in range(size - 1):
            num = (nums[i] + nums[i + 1]) % 10
            array.append(num)
        print(array)
        return self.triangularSum(array)


obj = Solution()

nums = [1,2,3,4,5]
expected = 8
result = obj.triangularSum(nums)
printResult(result, expected)

nums = [5]
expected = 5
result = obj.triangularSum(nums)
printResult(result, expected)
