from typing import List
from myUtils.Utils import printResult
from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        result = []
        minCharacter = "a"
        for c in s:
            stack.append(c)
            counter[c] -= 1
            while minCharacter != "z" and counter[minCharacter] == 0:
                minCharacter = chr(ord(minCharacter) + 1)
            # print(minCharacter)
            while stack and stack[-1] <= minCharacter:
                result.append(stack.pop())
        return "".join(result)       
        
        # arr = list(s)
        # if s.endswith("a"):
        #     idx = s.rfind("a")
        #     last = arr[:idx]
        #     return "".join(arr[idx:] + last[::-1])
        # arr.sort()
        # return "".join(arr)
        
obj = Solution()

s = "zza"
expected =  "azz"
result = obj.robotWithString(s)
printResult(result, expected)

s = "bac"
expected =  "abc"
result = obj.robotWithString(s)
printResult(result, expected)

s = "bdda"
expected =  "addb"
result = obj.robotWithString(s)
printResult(result, expected)

