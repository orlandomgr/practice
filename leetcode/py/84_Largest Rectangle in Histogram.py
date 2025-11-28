from typing import List
from myUtils.Utils import printResult

class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                # print("s: %s h: %s w: %s a: %s" %(i, h, w, h * w))
                ans = max(ans, h * w)
            stack.append(i)

        return ans
        

obj = Solution()

heights = [4,2,0,3,2,4,3,4]
expected = 10
result = obj.largestRectangleArea(heights)
printResult(result, expected)

heights = [2,1,5,6,2,3]
expected = 10
result = obj.largestRectangleArea(heights)
printResult(result, expected)

heights = [2,4]
expected = 4
result = obj.largestRectangleArea(heights)
printResult(result, expected)

