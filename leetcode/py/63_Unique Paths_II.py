from typing import List
from myUtils.Utils import printResult
from collections import deque


class Solution:
   def getMatrix(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
      rows = len(obstacleGrid)
      cols = len(obstacleGrid[0])
      for r in range(rows):
         for c in range(cols):
            if obstacleGrid[r][c] == 1:
               obstacleGrid[r][c] = -1
      return obstacleGrid

   def dp(self, m: int, n: int ):
      if self.matrix[m - 1][n - 1] < 0 or self.matrix[0][0] < 0:
         self.matrix[0][0] = 0
         return 
      self.matrix[m - 1][n - 1] = 1
      # for r in self.matrix:
      #    print(r)
      for r in range(self.m - 1, -1, -1):
         for c in range(self.n - 1, -1 , -1):
            down = 0
            if r < self.m - 1:
               down = self.matrix[r+1][c] if self.matrix[r+1][c] >= 0 else 0
            right = 0
            if c < self.n - 1:
               right = self.matrix[r][c+1] if self.matrix[r][c+1] >= 0 else 0

            if self.matrix[r][c] >= 0:   
               self.matrix[r][c] += down + right
      
   def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
      self.matrix = self.getMatrix(obstacleGrid)
      self.m = len(self.matrix)
      self.n = len(self.matrix[0])
      self.dp(self.m, self.n)
      # for r in self.matrix:
      #    print(r)
      return self.matrix[0][0]


obj = Solution()

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
expected = 2
result = obj.uniquePathsWithObstacles(obstacleGrid)
printResult(result, expected)

obstacleGrid = [[0,1],[0,0]]
expected = 1
result = obj.uniquePathsWithObstacles(obstacleGrid)
printResult(result, expected)

obstacleGrid = [[0,0],[0,1]]
expected = 0
result = obj.uniquePathsWithObstacles(obstacleGrid)
printResult(result, expected)

obstacleGrid = obstacleGrid = [[1]]
expected = 0
result = obj.uniquePathsWithObstacles(obstacleGrid)
printResult(result, expected)

obstacleGrid = [[1,0]]
expected = 0
result = obj.uniquePathsWithObstacles(obstacleGrid)
printResult(result, expected)
