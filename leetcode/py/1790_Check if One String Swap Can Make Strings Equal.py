from myUtils.Utils import printResult
from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        s1Counter = Counter(s1)
        s2Counter = Counter(s2)

        if s1Counter != s2Counter:
            return False
        
        n = len(s1)

        miss = 0
        for i in range(n):
            if s1[i] != s2[i]:
                miss += 1


        return True if miss == 2 else False
        
obj = Solution()

s1 = "bank"
s2 = "kanb"
expected = True
result = obj.areAlmostEqual(s1, s2)
printResult(result, expected)        

s1 = "attack"
s2 = "defend"
expected = False
result = obj.areAlmostEqual(s1, s2)
printResult(result, expected)        

s1 = "kelb"
s2 = "kelb"
expected = True
result = obj.areAlmostEqual(s1, s2)
printResult(result, expected)        

