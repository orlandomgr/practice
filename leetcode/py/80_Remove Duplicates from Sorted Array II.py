from typing import List
from myUtils.Utils import printResult

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      nums.sort()
      n = len(nums)
      i = 0
      j = 0
      last = 10**10
      count = 0
      while i < n:
         if nums[i] == last:
            count += 1
            

      return i
    
obj = Solution()

nums = [1,1,1,2,2,3]
expected = 5
result = obj.removeDuplicates(nums)
printResult(result,expected)

nums = [0,0,1,1,1,1,2,3,3]
expected = 7
result = obj.removeDuplicates(nums)
printResult(result,expected)
