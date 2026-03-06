from myUtils.Utils import printResult
from typing import List

"""
Given an m x n binary matrix mat, return the number of special positions in mat.

A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
"""
class Solution:
    def checkPos(self, mat: List[List[int]], row: int, col: int) -> bool:
        for r in range(len(mat)):
            if r != row and mat[r][col] == 1:
                return False
        
        for c in range(len(mat[0])):
            if c != col and mat[row][c] == 1:
                return False

        return True
    
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        rows = {}
        cols = {}

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if row in rows or col in cols:
                    continue
                if mat[row][col] == 1:
                    if self.checkPos(mat, row, col):
                        result += 1
                    else:
                        rows[row] = 1
                        cols[col] = 1

        return result

obj = Solution()

mat = [[1,0,0],[0,0,1],[1,0,0]]
expected = 1
result = obj.numSpecial(mat)
printResult(result, expected)

mat = [[1,0,0],[0,1,0],[0,0,1]]
expected = 3
result = obj.numSpecial(mat)
printResult(result, expected)
