from typing import List
from myUtils.Utils import printResult
from functools import cache

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        return 0

obj = Solution()

n=1
expected = 22
result = obj.nextBeautifulNumber(n)
printResult(result, expected)

n=1000
expected = 1333
result = obj.nextBeautifulNumber(n)
printResult(result, expected)

n=3000
expected = 3133
result = obj.nextBeautifulNumber(n)
printResult(result, expected)
