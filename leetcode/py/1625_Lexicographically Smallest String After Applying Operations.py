from typing import List
from myUtils.Utils import printResult
from functools import cache


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)

        def add(s: str, a: int):
            nums = [int(i) for i in s]
            for i in range(1, n, 2):
                nums[i] = (nums[i] + a) % 10
            s = "".join([str(i) for i in nums])
            # print("add: <%s>" %s)
            return s

        def rotate(s: str, b):
            rotations = b
            if b > n:
                rotations = b % n
            
            first = s[:rotations]
            last = s[rotations:]
            s = "".join(last + first)
            # print("rotate: <%s>" %s)
            return s

        known = set()
        def dfs(s: str):
            if s in known:
                return
            known.add(s)
            dfs(rotate(s, b))
            dfs(add(s, a))
            
        dfs(s)        
        return min(known)


obj = Solution()

s = "84688926"
a = 2
b = 5
expected = "00148068"
result = obj.findLexSmallestString(s, a, b)
printResult(result, expected)

s= "43987654"
a = 7
b = 3
expected = "00553311"
result = obj.findLexSmallestString(s, a, b)
printResult(result, expected)

s = "5525"
a = 9
b = 2
expected = "2050"
result = obj.findLexSmallestString(s, a, b)
printResult(result, expected)

s = "74"
a = 5
b = 1
expected = "24"
result = obj.findLexSmallestString(s, a, b)
printResult(result, expected)

s = "0011"
a = 4
b = 2
expected = "0011"
result = obj.findLexSmallestString(s, a, b)
printResult(result, expected)
