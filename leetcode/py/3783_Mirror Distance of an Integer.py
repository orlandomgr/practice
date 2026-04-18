from myUtils.Utils import printResult

"""
You are given an integer n.

Define its mirror distance as: abs(n - reverse(n))​​​​​​​ where reverse(n) is the integer formed by reversing the digits of n.

Return an integer denoting the mirror distance of n​​​​​​​.

abs(x) denotes the absolute value of x.
"""

class Solution:
    def mirrorDistance(self, n: int) -> int:
        r_num = int(str(n)[::-1])
        return abs(n - r_num)

obj = Solution()

n = 25
expected = 27
result = obj.mirrorDistance(n)
printResult(result, expected)

n = 10
expected = 9
result = obj.mirrorDistance(n)
printResult(result, expected)

n = 7
expected = 0
result = obj.mirrorDistance(n)
printResult(result, expected)


