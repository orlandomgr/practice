from myUtils.Utils import printResult

class Solution:
    def smallestNumber(self, n: int) -> int:
      binN = bin(n)
      n = len(binN) - 2
      return int( "".join(["1"] * n),2)

obj = Solution()

n = 5
expected = 7
result = obj.smallestNumber(n)
printResult(result, expected)        

n = 10
expected = 15
result = obj.smallestNumber(n)
printResult(result, expected)        

n = 3
expected = 3
result = obj.smallestNumber(n)
printResult(result, expected)        