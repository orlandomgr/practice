from typing import List
from myUtils.Utils import printResult

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def isSameDigits(s):
            arr = set(s)
            return len(arr) == 1
        
        def getNewNumbers(s):
            n = len(s)
            newN = []
            for i in range(1, n):
                n1 = int(s[i - 1])
                n2 = int(s[i])
                newN.append(str((n1 + n2) % 10))
            return "".join(newN)
        
        n = len(s)
        if n == 1:
            return True
        while n >= 2:
          s = getNewNumbers(s)
          n = len(s)
          if n >= 2:
            res = isSameDigits(s)
            if res: return res
        return False
    
obj = Solution()

s = "3902"
expected = True
result = obj.hasSameDigits(s)
printResult(result, expected)

s = "34789"
expected = False
result = obj.hasSameDigits(s)
printResult(result, expected)
