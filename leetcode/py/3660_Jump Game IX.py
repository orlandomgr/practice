from myUtils.Utils import printResult
from typing import List
"""
You are given an integer array nums.

From any index i, you can jump to another index j under the following rules:

* Jump to index j where j > i is allowed only if nums[j] < nums[i].
* Jump to index j where j < i is allowed only if nums[j] > nums[i].
For each index i, find the maximum value in nums that can be reached by following any sequence of valid jumps starting at i.

Return an array ans where ans[i] is the maximum value reachable starting from index i.
"""

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        stack = []

        for i in range(n):
            curr = nums[i]
            currL = i
            currR = i

            while stack and stack[-1][0] > nums[i]:
                topVal, topLeft, topRight = stack.pop()
                curr = max (curr, topVal)
                currL = topLeft
            
            stack.append((curr, currL, currR))

        for i in range(len(stack)):
            for j in range(stack[i][1], stack[i][2] + 1):
                result[j] = stack[i][0]

        return result

obj = Solution()

nums = [2,1,3]
expected = [2,2,3]
result = obj.maxValue(nums)
printResult(result, expected)

nums = [2,3,1]
expected = [3,3,3]
result = obj.maxValue(nums)
printResult(result, expected)

