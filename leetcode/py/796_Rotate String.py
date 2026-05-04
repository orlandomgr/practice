from typing import List
from myUtils.Utils import printResult

"""
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 """

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        listS = list(s)
        listG = list(goal)
        setS = set(listS)
        setG = set(listG)

        if setS != setG or len(s) != len(goal):
            return False

        def checkIndices(g):
            for i in range(len(s)):
                if s[i] != goal[g]:
                    return False
                g += 1
                if g == len(s):
                    g = 0
            return True
        
        indices = [i for i, x in enumerate(list(goal)) if x == s[0]]
        while indices:
            i = indices.pop()  
            if checkIndices(i):
                return True

        return False

obj = Solution()

s = "abcde"
goal = "cdeab"
expected = True
result = obj.rotateString(s, goal)
printResult(result, expected)

s = "abcde"
goal = "abced"
expected = False
result = obj.rotateString(s, goal)
printResult(result, expected)

