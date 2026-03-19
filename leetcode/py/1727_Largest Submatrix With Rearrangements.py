from typing import List
from myUtils.Utils import printResult

"""
You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.
"""
class Solution:    

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        result = 0

        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]

        for r in range(rows):
            matrix[r].sort(reverse=True)
            for c in range(cols):
                result = max(result, matrix[r][c] * (c + 1))

        return result


obj = Solution()

matrix = [[0,0,1],[1,1,1],[1,0,1]]
expected = 4
result = obj.largestSubmatrix(matrix)
printResult(result, expected)

matrix = [[1,0,1,0,1]]
expected = 3
result = obj.largestSubmatrix(matrix)
printResult(result, expected)

matrix = [[1,1,0],[1,0,1]]
expected = 2
result = obj.largestSubmatrix(matrix)
printResult(result, expected)
