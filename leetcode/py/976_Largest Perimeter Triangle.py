from typing import List
from myUtils.Utils import printResult

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        size = len(nums)
        nums.sort()
        result = 0

        i = size - 1
        while i >= 2:
            if nums[i] < nums[i-1] + nums[i-2]:
                # print("size: %s i: %s j: %s k: %s" %(size, i, j, k))
                return nums[i] + nums[i-1] + nums[i-2]
            i -= 1

        return result

obj = Solution()

nums = [1,4,18,3,8,4,4]
expected = 12
result = obj.largestPerimeter(nums)
printResult(result, expected)        

nums = [3,4,15,2,9,4]
expected = 11
result = obj.largestPerimeter(nums)
printResult(result, expected)        

nums = [2,1,2]
expected = 5
result = obj.largestPerimeter(nums)
printResult(result, expected)        

nums = [1,2,1,10]
expected = 0
result = obj.largestPerimeter(nums)
printResult(result, expected)        
