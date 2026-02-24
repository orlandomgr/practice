from myUtils.Utils import printResult

class Solution:

 def binaryGap(self, n: int) -> int:
    binary_string = bin(n)[2:]

    maxLen = 0
    i = binary_string.find("1", 0)
    while i < len(binary_string):
        j = binary_string.find("1", i + 1)
        maxLen = max(maxLen, j - i)
        if j == -1:
           break
        i = j

    return maxLen
        
obj = Solution()

n = 22
expected = 2
result = obj.binaryGap(n)
printResult(result, expected)

n = 8
expected = 0
result = obj.binaryGap(n)
printResult(result, expected)

n = 5
expected = 2
result = obj.binaryGap(n)
printResult(result, expected)
