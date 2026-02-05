from typing import List
from myUtils.Utils import printResult
from collections import defaultdict, Counter, OrderedDict
import heapq

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n, 2):
            # print(i)
            if nums[i] != nums[i-1]:
                return nums[i-1]
        return nums[-1]

obj = Solution()

nums = [1,1,2,2,3,3,4,4,8]
expected = 8
result = obj.singleNonDuplicate(nums)
printResult(result, expected)

nums = [1,2,2,3,3,4,4,8,8]
expected = 1
result = obj.singleNonDuplicate(nums)
printResult(result, expected)

nums = [1,1,2,3,3,4,4,8,8]
expected = 2
result = obj.singleNonDuplicate(nums)
printResult(result, expected)

nums = [1,1,2,3,3,4,4,8,8]
expected = 2
result = obj.singleNonDuplicate(nums)
printResult(result, expected)

nums = [3,3,7,7,10,11,11]
expected = 10
result = obj.singleNonDuplicate(nums)
printResult(result, expected)
