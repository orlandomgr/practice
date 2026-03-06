from myUtils.Utils import printResult

"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
"""
class Solution:
    def minOperations(self, s: str) -> int:
        result1 = 0
        result2 = 0
        prev1 = "1"
        prev2 = "0"
        for i in range(len(s)):
            if s[i] == prev1:
                result1 += 1
                prev1 = "0" if s[i] == "1" else "1"
            else:
                prev1 = s[i]
            if s[i] == prev2:
                result2 += 1
                prev2 = "0" if s[i] == "1" else "1"
            else:
                prev2 = s[i]

        print(f"r1: {result1} r2: {result2}")

        return min(result1, result2)

obj = Solution()

s = "10010100"
expected = 3
result = obj.minOperations(s)
printResult(result, expected)

s = "1000"
expected = 1
result = obj.minOperations(s)
printResult(result, expected)

s = "0100"
expected = 1
result = obj.minOperations(s)
printResult(result, expected)

s = "10"
expected = 0
result = obj.minOperations(s)
printResult(result, expected)

s = "1111"
expected = 2
result = obj.minOperations(s)
printResult(result, expected)
