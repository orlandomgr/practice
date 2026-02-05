from myUtils.Utils import printResult

class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0 and len(s) == 0:
            return True
        if len(p) == 0:
            return False
        rows = len(s)
        cols = len(p)
        matrix = [[None] * (cols + 1) for _ in range(rows + 1)]

        # for row in matrix:
        #     print(row)

        def dp(i, j):
            if matrix[i][j] is not None:
                return matrix[i][j]
            
            if j == len(p):
                return i == len(s)
            if i == len(s):
                if (len(p) - j) % 2 == 1:
                    return False
                for k in range(j + 1, len(p), 2):
                    if p[k] != "*":
                        return False
                return True

            match = s[i] == p[j] or p[j] == "."

            if j < len(p) - 1 and p[j + 1] == "*":
                result = dp(i, j + 2) or (match and dp(i + 1, j))
            else:
                result = match and dp(i + 1, j + 1)
  
            matrix[i][j] = result
            return result

        res = dp(0, 0)

        # for row in matrix:
        #     print(row)

        return res


obj = Solution()

s = "aa"
p = "a"
expected = False
result = obj.isMatch(s, p)
printResult(result, expected)

s = "aa"
p = "a*"
expected = True
result = obj.isMatch(s, p)
printResult(result, expected)

s = "ab"
p = ".*"
expected = True
result = obj.isMatch(s, p)
printResult(result, expected)

s = "abczz"
p = ".*zz"
expected = True
result = obj.isMatch(s, p)
printResult(result, expected)
