from myUtils.Utils import printResult

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary_string = bin(n)
        prev = binary_string[0]
        for i in range(1, len(binary_string)):
            if binary_string[i] == prev:
                return False
            prev = binary_string[i]
        return True

obj = Solution()

n = 5
expected = True
result = obj.hasAlternatingBits(n)
printResult(result, expected)

n = 7
expected = False
result = obj.hasAlternatingBits(n)
printResult(result, expected)

n = 11
expected = False
result = obj.hasAlternatingBits(n)
printResult(result, expected)
