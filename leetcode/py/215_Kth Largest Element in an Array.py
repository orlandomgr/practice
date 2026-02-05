from typing import List
from myUtils.Utils import printResult
import heapq
import math 
from itertools import combinations
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = [] 

        for num in nums:
            heapq.heappush(pq, -num)
        for _ in range(k - 1):
            heapq.heappop(pq)
        return -heapq.heappop(pq)


obj = Solution()

nums = [3,2,1,5,6,4]
k = 2
expected = 5
result = obj.findKthLargest(nums, k)
printResult(result, expected)

nums = [3,2,3,1,2,4,5,5,6]
k = 4
expected = 4
result = obj.findKthLargest(nums, k)
printResult(result, expected)

