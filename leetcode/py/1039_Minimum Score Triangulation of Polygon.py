from typing import List
from myUtils.Utils import printResult
from functools import cache

class Solution:

    def minScoreTriangulation(self, values: List[int]) -> int:
        size = len(values)

        @cache
        def dfs(i: int, j: int):
            if i + 1  == j:
                return 0
            minResult = 10 ** 10
            for k in range(i + 1, j):
                current = dfs(i, k) + dfs(k, j) + (values[i] * values[j] * values[k])
                minResult = min(minResult, current)
            return minResult

        return dfs(0, size - 1)


obj = Solution()


values = [35,73,90,27,71,80,21,33,33,13,48,12,68,70,80,36,66,3,70,58]
expected = 140295
result = obj.minScoreTriangulation(values)
printResult(result, expected)

values = [2,1,4,4]
expected = 24
result = obj.minScoreTriangulation(values)
printResult(result, expected)


values = [3,4,4,4]
expected = 96
result = obj.minScoreTriangulation(values)
printResult(result, expected)

values = [1, 2, 3]
expected = 6
result = obj.minScoreTriangulation(values)
printResult(result, expected)

values = [3, 7, 4, 5]
expected = 144
result = obj.minScoreTriangulation(values)
printResult(result, expected)

values = [1, 3, 1, 4, 1, 5]
expected = 13
result = obj.minScoreTriangulation(values)
printResult(result, expected)
