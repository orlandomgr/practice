from myUtils.Utils import printResult
from typing import List

"""
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.
"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if n == 0 or s[0] != '0':
            return False

        reachable = [False] * n
        reachable[0] = True
        window_reachable = 0

        for i in range(1, n):
            if i - minJump >= 0 and reachable[i - minJump]:
                window_reachable += 1
            if i - maxJump - 1 >= 0 and reachable[i - maxJump - 1]:
                window_reachable -= 1

            if window_reachable > 0 and s[i] == '0':
                reachable[i] = True

        return reachable[-1]

obj = Solution()

s = "011010"
minJump = 2
maxJump = 3
expected = True
result = obj.canReach(s, minJump, maxJump)
printResult(result, expected)

s = "01101110"
minJump = 2
maxJump = 3
expected = False
result = obj.canReach(s, minJump, maxJump)
printResult(result, expected)

