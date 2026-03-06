from myUtils.Utils import printResult

"""
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.
"""
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        res = s.split("0")
        res = list(filter(None, res))
        return len(res) == 1

obj = Solution()

s = "1100111"
expected = False
result = obj.checkOnesSegment(s)
printResult(result, expected)

s = "1001"
expected = False
result = obj.checkOnesSegment(s)
printResult(result, expected)

s = "110"
expected = True
result = obj.checkOnesSegment(s)
printResult(result, expected)

