from typing import List
from myUtils.Utils import printResult
import heapq

"""
You are given an m x n integer matrix grid​​​.
A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:
Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.
Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.
"""
class Solution:    
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        pq = []

        def getRhombusSum(row:int, col:int) -> List[int]:
            maxSize= min(col + 1, cols - col, (rows - row + 1) // 2 )

            for t in range(maxSize):
                if t == 0: 
                    heapq.heappush(pq, -grid[row][col])
                    continue
                curr = 0
                currR, currC = row, col
                for _ in range(t): # down - left
                    curr += grid[currR][currC]
                    currR +=1
                    currC -=1
                for _ in range(t): # down - right
                    curr += grid[currR][currC]
                    currR +=1
                    currC +=1
                for _ in range(t): # up - right
                    curr += grid[currR][currC]
                    currR -=1
                    currC +=1
                for _ in range(t): # up - left
                    curr += grid[currR][currC]
                    currR -=1
                    currC -=1
                heapq.heappush(pq, -curr)
            return 

        result = set()
        for row in range(rows):
            for col in range(cols):
                getRhombusSum(row, col)
                
        while pq and len(result) < 3:
            area = -heapq.heappop(pq)
            result.add(area)
        return sorted(list(result), reverse=True)

obj = Solution()

grid = [
    [3,4,5,1,3],
    [3,3,4,2,3],
    [20,30,200,40,10],
    [1,5,5,4,1],
    [4,3,2,2,5]
    ]
expected = [228,216,211]
result = obj.getBiggestThree(grid)
printResult(result, expected)

grid = [[1,2,3],[4,5,6],[7,8,9]]
expected = [20,9,8]
result = obj.getBiggestThree(grid)
printResult(result, expected)

grid = [[7,7,7]]
expected = [7]
result = obj.getBiggestThree(grid)
printResult(result, expected)
