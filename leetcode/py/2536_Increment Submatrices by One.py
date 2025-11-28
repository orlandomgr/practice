from typing import List
from myUtils.Utils import printResult
from itertools import accumulate

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [] 
        for _ in range(n + 1):
            matrix.append([0] * n)
        # print(matrix)
        for r1, c1, r2, c2 in queries:
            # print("r1: %s c1: %s r2: %s c2:%s " %(r1, c1, r2, c2))
            matrix[r1][c1] += 1
            matrix[r2+1][c1] -= 1
            if c2+1<n:
                matrix[r1][c2+1]-=1
                matrix[r2+1][c2+1]+=1

        for i in range(n):
            matrix[i] = list(accumulate(matrix[i]))

        for j in range(n):
            for i in range(1, n):
                matrix[i][j] += matrix[i-1][j]

        return matrix[:n]

obj = Solution()

n = 3
queries = [[1,1,2,2],[0,0,1,1]]
expected = [[1,1,0],[1,2,1],[0,1,1]]
result = obj.rangeAddQueries(n, queries)
printResult(result, expected)

n = 2
queries = [[0,0,1,1]]
expected = [[1,1],[1,1]]
result = obj.rangeAddQueries(n, queries)
printResult(result, expected)
