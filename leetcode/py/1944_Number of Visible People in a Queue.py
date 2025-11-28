from myUtils.Utils import printResult
from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0] * n

        stack = []

        for i in range(n - 1, -1, -1):
            # print(heights[i])
            current = heights[i]

            while stack and stack[-1] < current:
                result[i] += 1
                stack.pop()

            if stack:
                result[i] += 1

            stack.append(current)

        return result


obj = Solution()

heights = [10, 6, 8, 5, 11, 9]
expected = [3, 1, 2, 1, 1, 0]
result = obj.canSeePersonsCount(heights)
printResult(result, expected)

heights = [5, 1, 2, 3, 10]
expected = [4, 1, 1, 1, 0]
result = obj.canSeePersonsCount(heights)
printResult(result, expected)
