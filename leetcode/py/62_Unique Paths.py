from typing import List
from myUtils.Utils import printResult
from collections import deque


class Solution:
   def getMatrix(self, m: int, n: int) -> List[List[int]]:
      matrix = []
      for _ in range(m):
         matrix.append([0] * n)
      return matrix

   def dp(self, m: int, n: int ):
      self.matrix[m - 1][n - 1] = 1
      # for r in self.matrix:
      #    print(r)
      for r in range(self.m - 1, -1, -1):
         for c in range(self.n - 1, -1 , -1):
            down = 0
            if r < self.m - 1:
               down = self.matrix[r+1][c]
            right = 0
            if c < self.n - 1:
               right = self.matrix[r][c+1]
            self.matrix[r][c] += down + right
      
   def uniquePaths(self, m: int, n: int) -> int:
      self.matrix = self.getMatrix(m, n)
      self.m = m
      self.n = n
      self.dp(m, n)
      # for r in self.matrix:
      #    print(r)
      return self.matrix[0][0]


obj = Solution()

m = 3
n = 7
expected = 28
result = obj.uniquePaths(m, n)
printResult(result, expected)

m = 3
n = 2
expected = 3
result = obj.uniquePaths(m, n)
printResult(result, expected)

m = 23
n = 12
expected = 193536720
result = obj.uniquePaths(m, n)
printResult(result, expected)
