from typing import List
from myUtils.Utils import printResult
from functools import cache
import time
from collections import defaultdict, deque
import heapq
import math


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        maxSum = 0
        subs = 10 ** 10
        counter = 0

        for num in nums:
            newN = num ^ k
            if newN > num:
                maxSum += newN
                subs = min(subs, newN - num)
                counter += 1
            else:
                maxSum += num
                subs = min(subs, num - newN)

        if counter % 2 == 0:
            return maxSum
        else:
            return maxSum - subs
        

        # for x, y in edges:
        #     newX = nums[x] ^ k
        #     newY = nums[y] ^ k
        #     if newX > nums[x]:
        #         nums[x] = newX
        #     if newY > nums[y]:
        #         nums[y] = newY
        #     print(nums)
        #     maxSum = max(maxSum, sum(nums))

        # return maxSum


obj = Solution()

nums = [24,78,1,97,44]
k = 6
edges = [[0,2],[1,2],[4,2],[3,4]]
expected = 260
result = obj.maximumValueSum(nums, k, edges)
printResult(result, expected)

nums = [1, 2, 1]
k = 3
edges = [[0, 1], [0, 2]]
expected = 6
result = obj.maximumValueSum(nums, k, edges)
printResult(result, expected)

nums = [2, 3]
k = 7
edges = [[0, 1]]
expected = 9
result = obj.maximumValueSum(nums, k, edges)
printResult(result, expected)

nums = [7, 7, 7, 7, 7, 7]
k = 3
edges = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]
expected = 42
result = obj.maximumValueSum(nums, k, edges)
printResult(result, expected)
