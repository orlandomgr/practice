from myUtils.Utils import printResult
from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n = len(s)

        sCounter = Counter(s)
        gCounter = Counter(goal)

        if sCounter != gCounter:
            return False

        if n < 2:
            return False
        
        repeat = 0
        for _, count in sCounter.items():
            if count >= 2:
                repeat += 1
                break

        miss = 0
        for i in range(n):
            if s[i] != goal[i]:
                miss += 1
        
        return True if miss == 2 or (miss == 0 and repeat >= 1) else False

obj = Solution()

s = "abab"
goal = "baba"
expected = False
result = obj.buddyStrings(s, goal)
printResult(result, expected)

s = "abab"
goal = "abab"
expected = True
result = obj.buddyStrings(s, goal)
printResult(result, expected)

s = "abcaa"
goal = "abcbb"
expected = False
result = obj.buddyStrings(s, goal)
printResult(result, expected)

s = "ab"
goal = "ba"
expected = True
result = obj.buddyStrings(s, goal)
printResult(result, expected)

s = "ab"
goal = "ab"
expected = False
result = obj.buddyStrings(s, goal)
printResult(result, expected)

s = "aa"
goal = "aa"
expected = True
result = obj.buddyStrings(s, goal)
printResult(result, expected)

