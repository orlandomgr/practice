from typing import List
from myUtils.Utils import printResult
from collections import deque


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == t[j]:
                cache[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                cache[(i, j)] = dfs(i + 1, j)
            return cache[(i, j)]

        return dfs(0, 0)


obj = Solution()

s = "rabbbit"
t = "rabbit"
expected = 3
result = obj.numDistinct(s, t)
printResult(result, expected)

s = "babgbag"
t = "bag"
expected = 5
result = obj.numDistinct(s, t)
printResult(result, expected)
