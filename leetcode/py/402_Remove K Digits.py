from typing import List
from myUtils.Utils import printResult
import heapq
import math 
from itertools import combinations

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []

        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)

        stack = stack[:len(stack) - k]
        res = "".join(stack)
        res = res.lstrip('0')
        return res if res else "0"


obj = Solution()

num = "112"
k = 1
expected = "11"
result = obj.removeKdigits(num, k)
printResult(result, expected)

num = "33526221184202197273"
k = 19
expected = "0"
result = obj.removeKdigits(num, k)
printResult(result, expected)

num = "1432219"
k = 3
expected = "1219"
result = obj.removeKdigits(num, k)
printResult(result, expected)

num = "10200"
k = 1
expected = "200"
result = obj.removeKdigits(num, k)
printResult(result, expected)

num = "10"
k = 2
expected = "0"
result = obj.removeKdigits(num, k)
printResult(result, expected)

