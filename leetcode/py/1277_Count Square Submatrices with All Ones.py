from typing import List

class Solution:

    def countSquaresSize(self, matrix: List[List[int]], size) -> int:
        counter = 0
        rowSize = len(matrix)
        colSize = len(matrix[0])
        for rowIdx, rowValue in enumerate(matrix):
            if rowIdx > rowSize - size:
                continue
            for colIdx, colValue in enumerate(matrix[0]):
                if colIdx > colSize - size:
                    continue

                # print("row: %s col: %s val: %s" %(rowIdx, colIdx, matrix[rowIdx][colIdx]))
                count = False
                shouldExit = False
                # if size > 1:
                if matrix[rowIdx][colIdx] == 1:
                    count = True
                    for r in range(size):
                        if shouldExit: 
                            break
                        for c in range(size):
                            if matrix[rowIdx+r][colIdx+c] == 0:
                                count = False
                                shouldExit = True
                                # rowIdx = r 
                                colIdx = c 
                                break

                if count:
                    counter += 1

        return counter



    def countSquares(self, matrix: List[List[int]]) -> int:
        counter = 0
        for i in range(1, len(matrix) + 1):
            level = self.countSquaresSize(matrix, i)
            counter += level
            if level == 0:
                break
            print("i: %s count: %s" %(i, level))
        return counter



obj = Solution()
matrix = \
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
print(obj.countSquares(matrix))

matrix = \
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
print(obj.countSquares(matrix))

