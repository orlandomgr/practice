from myUtils.Utils import printResult
import math 

class Solution:
    def countOrders(self, n: int) -> int:
        res = math.factorial(n * 2)
        res = res // 2 ** n
        return res % (10**9 + 7)
       
obj = Solution()

n = 1
expected = 1
result = obj.countOrders(n)
printResult(result, expected)

n = 2
expected = 6
result = obj.countOrders(n)
printResult(result, expected)

n = 3
expected = 90
result = obj.countOrders(n)
printResult(result, expected)

