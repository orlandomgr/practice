from typing import List
from myUtils.Utils import printResult
from collections import deque


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        rows = len(s)
        cols = len(p)

        dp = [[False] * (cols + 1) for _ in range(rows + 1)]
        dp[0][0] = True

        for j in range(1, cols + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        # for row in dp:
        #     print(row)

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif p[j - 1] == "?" or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        # for row in dp:
        #     print(row)

        return dp[rows][cols]


obj = Solution()

# s = "aa"
# p = "a"
# expected = False
# result = obj.isMatch(s, p)
# printResult(result, expected)

s = "aa"
p = "*"
expected = True
result = obj.isMatch(s, p)
printResult(result, expected)

# s = "cb"
# p = "?a"
# expected = False
# result = obj.isMatch(s, p)
# printResult(result, expected)
