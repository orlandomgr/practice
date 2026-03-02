from myUtils.Utils import printResult


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        arr = []
        for i in range(1, n + 1):
            arr.append(bin(i)[2:])
        num = int("".join(arr), 2)

        return num % (10**9 + 7)


obj = Solution()

n = 1
expected = 1
result = obj.concatenatedBinary(n)
printResult(result, expected)

n = 3
expected = 27
result = obj.concatenatedBinary(n)
printResult(result, expected)

n = 12
expected = 505379714
result = obj.concatenatedBinary(n)
printResult(result, expected)
