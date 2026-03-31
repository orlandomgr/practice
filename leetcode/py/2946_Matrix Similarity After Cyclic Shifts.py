from typing import List
from myUtils.Utils import printResult
from functools import cache
from collections import deque
import queue

"""
You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.

The following proccess happens k times:

Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.


Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.


Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

"""
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        original = mat.copy()
        n = len(mat)
        m = len(mat[0])
        def rotate(mat, dir):
            d = deque(mat)
            d.rotate(dir)
            return list(d)

        limit = k % m

        for _ in range(limit):
            for r in range(n):
                if r % 2 == 0:
                    mat[r] = rotate(mat[r], -1)
                else:
                    mat[r] = rotate(mat[r], 1)

        return original == mat


obj = Solution()

mat = [[5,8,8,4,7,2,3,4,3,10],[8,7,9,1,3,4,2,6,6,9],[6,2,10,10,4,6,3,4,1,1]]
k = 3
expected = False
result = obj.areSimilar(mat, k)
printResult(result, expected)

mat = [[1,2,3],[4,5,6],[7,8,9]]
k = 4
expected = False
result = obj.areSimilar(mat, k)
printResult(result, expected)

mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
k = 2
expected = True
result = obj.areSimilar(mat, k)
printResult(result, expected)

mat = [[2,2],[2,2]]
k = 3
expected = True
result = obj.areSimilar(mat, k)
printResult(result, expected)
