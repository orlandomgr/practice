from myUtils.Utils import printResult
from math import pow
import itertools

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        perms = list(itertools.permutations(s, len(s)))
        permsList = ["".join(p) for p in perms]
        permsList = [item for item in permsList if item[0] >= s[0]]
        permsList.sort()
        # print(permsList)
        for option in permsList:
            # print(option)
            if int(option) > n:
                if int(option) <= pow(2, 31) - 1:
                    return int(option)
                else:
                    return -1
        # print(p)
        return -1

obj = Solution()

n = 2147483486
expected = -1
result = obj.nextGreaterElement(n)
printResult(result, expected)

n = 230241
expected = 230412
result = obj.nextGreaterElement(n)
printResult(result, expected)

n = 12
expected = 21
result = obj.nextGreaterElement(n)
printResult(result, expected)

n = 21
expected = -1
result = obj.nextGreaterElement(n)
printResult(result, expected)