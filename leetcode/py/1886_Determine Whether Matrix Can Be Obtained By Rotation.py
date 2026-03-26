from typing import List
from myUtils.Utils import printResult

"""
Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.
"""
class Solution:    

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix: List[List[int]]) -> List[List[int]]:
            n = len(matrix)
            for r in range(n):
                for c in range(r, n):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            for r in range(n):
                matrix[r].reverse()
            return matrix

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)

        return False
   

obj = Solution()

mat = [[0,1],[1,0]]
target = [[1,0],[0,1]]
expected = True
result = obj.findRotation(mat, target)
printResult(result, expected)

mat = [[0,1],[1,1]]
target = [[1,0],[0,1]]
expected = False
result = obj.findRotation(mat, target)
printResult(result, expected)

mat = [[0,0,0],[0,1,0],[1,1,1]]
target = [[1,1,1],[0,1,0],[0,0,0]]
expected = True
result = obj.findRotation(mat, target)
printResult(result, expected)
