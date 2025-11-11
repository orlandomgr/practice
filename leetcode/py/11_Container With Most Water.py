from typing import List
from myUtils.Utils import printResult

class Solution:
    def maxArea(self, height: List[int]) -> int:
        size = len(height)

        maxArea = 0
        i = 0
        j = size - 1
        while i < j:
            maxArea = max(maxArea, (min(height[i], height[j]) * (j - i)))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea


obj = Solution()

height = [1, 3, 2, 5, 25, 24, 5]
expected = 24
result = obj.maxArea(height)
printResult(result, expected)

height = [1,8,6,2,5,4,8,3,7]
expected = 49
result = obj.maxArea(height)
printResult(result,expected)

height = [1,1]
expected = 1
result = obj.maxArea(height)
printResult(result,expected)

height = [1,2,1]
expected = 2
result = obj.maxArea(height)
printResult(result,expected)

height = [3,6,1]
expected = 3
result = obj.maxArea(height)
printResult(result,expected)

height = [1,2,4,3]
expected = 4
result = obj.maxArea(height)
printResult(result,expected)
