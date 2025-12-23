from typing import List
from myUtils.Utils import printResult

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix    
        n = len(matrix)
        if n == 0:
            self.prefix = []
            return 
        
        m = len(matrix[0])
        self.prefix = [[0] * (m+1) for _ in range(n)]
        for r in range(n):
            for c in range(m):
                self.prefix[r][c+1] = self.prefix[r][c] + matrix[r][c]

        # for r in range(n):
        #     print(self.prefix[r])

        # self.cacheSum = {}
        # self.cacheRow = {}

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # if (row1,col1,row2,col2) in self.cacheSum:
        #     return self.cacheSum[(row1,col1,row2,col2)]
        result = 0
        for r in range(row1, row2 + 1):
            # if (i,col1,col2) not in self.cacheRow:
            #     self.cacheRow[(i,col1,col2)] = sum(self.matrix[i][col1:col2+1])
            # result += self.cacheRow[(i,col1,col2)]    
            result += self.prefix[r][col2+1] - self.prefix[r][col1]
        return result

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

numMatrix = NumMatrix(
    [
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, 2, 0, 1, 5], 
    [4, 1, 0, 1, 7], 
    [1, 0, 3, 0, 5]
    ])
result = numMatrix.sumRegion(2, 1, 4, 3) # return 8 (i.e sum of the red rectangle)
printResult(result, 8)
result = numMatrix.sumRegion(1, 1, 2, 2) # return 11 (i.e sum of the green rectangle)
printResult(result, 11)
result = numMatrix.sumRegion(1, 2, 2, 4) # return 12 (i.e sum of the blue rectangle)
printResult(result, 12)

numMatrix = NumMatrix(
    [[-4,-5]]
)
result = numMatrix.sumRegion(0,0,0,0) # return 8 (i.e sum of the red rectangle)
printResult(result, -4)
result = numMatrix.sumRegion(0,0,0,1) # return 11 (i.e sum of the green rectangle)
printResult(result, -9)
result = numMatrix.sumRegion(0,1,0,1) # return 12 (i.e sum of the blue rectangle)
printResult(result, -5)
