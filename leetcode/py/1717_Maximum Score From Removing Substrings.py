from typing import List
from myUtils.Utils import printResult


class Solution:
    def processString(self, s: str, f: str, price:int) :
        stack = []
        result = 0
        for c in s:
            if c == f[1]:
                if stack and stack[-1] == f[0]:
                    stack.pop()
                    result += price
                    continue
            stack.append(c)
        return "".join(stack), result


    def maximumGain(self, s: str, x: int, y: int) -> int:
        # "ab" and gain x
        # "ba" and gain y
        result = 0
        xStr = "ab"
        yStr = "ba"
        if x > y:
            findFirst = xStr
            findSecond = yStr
        else:
            findFirst = yStr
            findSecond = xStr
            tmp = x
            x = y
            y = tmp

        while s.find(findFirst) != -1 or s.find(findSecond) != -1:
            while s.find(findFirst) != -1:
                s, count = self.processString(s, findFirst, x)
                result += count

            while s.find(findSecond) != -1:
                s, count = self.processString(s, findSecond, y)
                result += count

        return result


obj = Solution()

s = "cdbcbbaaabab"
x = 4
y = 5
expected = 19
result = obj.maximumGain(s, x, y)
printResult(result, expected)

s = "aabbaaxybbaabb"
x = 5
y = 4
expected = 20
result = obj.maximumGain(s, x, y)
printResult(result, expected)
