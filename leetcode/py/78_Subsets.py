from typing import List
from myUtils.Utils import printResult
from collections import deque
import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        # result.append([])

        for i in range(len(nums) + 1):
            for combo in itertools.combinations(nums, i):
                result.append(list(combo))
                # print(list(combo))

        # result.sort()
        return result

obj = Solution()

nums = [1,2,3]
expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
result = obj.subsets(nums)
printResult(result, expected)

nums = [0]
expected = [[],[0]]
result = obj.subsets(nums)
printResult(result, expected)

