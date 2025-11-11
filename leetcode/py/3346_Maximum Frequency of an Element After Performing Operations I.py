from typing import List
from myUtils.Utils import printResult
from functools import cache
from collections import Counter
import queue
import math


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
      nums.sort()
      n = len(nums)
      if n < 2:
        return n
      options = [i for i in range(-k, k)]

      def getFreq(nums: List[int]):
          freq = {}
          for num in nums:
              if num not in freq:
                  freq[num] = 0
              freq[num] += 1
          return freq     

      freq = getFreq(nums)
      print(options)
      maxCount = max(freq.values())

      i = 0
      m = len(options)
      while i < numOperations:
        for o in range(m - 1):
          option = options[o]
          for i in range(n - 1):
            num = nums[i]
            newN = num + option
            addition = 1 if num != newN else 0 
            if option == 17:
              print("num:%s newN:%s option:%s" %(num,newN, option))
            if (nums.count(newN) + addition) > maxCount:
              i +=1 
              maxCount = nums.count(newN) + addition
            for j in range(m):
              if o == j:
                 continue  
              option2 = options[j]
              for k in range(i+1, n):
                num2 = nums[k]
                newN2 = num2 + option2
                addition2 = 1 if num2 != newN2 else 0 
                if option == 17 and option2 == -18:
                  print("num2:%s newN2:%s option2:%s" %(num2,newN2,option2))
                if (nums.count(newN2) + addition2) > maxCount:
                  i +=1 
                  maxCount = nums.count(newN2) + addition2
               
        break
      return maxCount
    

obj = Solution()

nums = [88, 53]
k = 27
numOperations = 2
expected = 2
result = obj.maxFrequency(nums, k, numOperations)
printResult(result, expected)

# nums = [18,57]
# k = 97
# numOperations = 2
# expected = 1
# result = obj.maxFrequency(nums, k, numOperations)
# printResult(result, expected)

# nums = [2,49]
# k = 97
# numOperations = 0
# expected = 1
# result = obj.maxFrequency(nums, k, numOperations)
# printResult(result, expected)

# nums = [3] 
# k = 2
# numOperations = 1
# expected = 1
# result = obj.maxFrequency(nums, k, numOperations)
# printResult(result, expected)

# nums = [1,4,5] 
# k = 1
# numOperations = 2
# expected = 2
# result = obj.maxFrequency(nums, k, numOperations)
# printResult(result, expected)

# nums = [5,11,20,20]
# k = 5
# numOperations = 1
# expected = 2
# result = obj.maxFrequency(nums, k, numOperations)
# printResult(result, expected)
