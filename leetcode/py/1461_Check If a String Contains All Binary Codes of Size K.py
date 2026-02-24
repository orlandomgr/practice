from myUtils.Utils import printResult
import itertools

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        prefix = set()
        for combo in itertools.product("01", repeat=k):
            prefix.add("".join(combo))

        for i in range(len(s) - k + 1):
            if s[i:i+k] in prefix:
                prefix.discard(s[i:i+k])

        if len(prefix) > 0:
            return False

        return True        

        
obj = Solution()

s = "00110110"
k = 2
expected = True
result = obj.hasAllCodes(s, k)
printResult(result, expected)

s = "0110"
k = 1
expected = True
result = obj.hasAllCodes(s, k)
printResult(result, expected)

s = "0110"
k = 2
expected = False
result = obj.hasAllCodes(s, k)
printResult(result, expected)
