from typing import List
from myUtils.Utils import printResult
from functools import reduce
from operator import xor
"""
You are given an integer array nums of length n and a 2D integer array queries of size q, where queries[i] = [li, ri, ki, vi].

For each query, you must apply the following operations in order:

Set idx = li.
While idx <= ri:
Update: nums[idx] = (nums[idx] * vi) % (109 + 7)
Set idx += ki.
Return the bitwise XOR of all elements in nums after processing all queries.
"""
class Solution:    

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for li, ri, ki, vi in queries:
            idx = li
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % (10**9 + 7)
                idx += ki
        
        return reduce(xor, nums)
   

obj = Solution()

nums = [1,1,1]
queries = [[0,2,1,4]]
expected = 4
result = obj.xorAfterQueries(nums, queries)
printResult(result, expected)

nums = [2,3,1,5,4]
queries = [[1,4,2,3],[0,2,1,2]]
expected = 31
result = obj.xorAfterQueries(nums, queries)
printResult(result, expected)

