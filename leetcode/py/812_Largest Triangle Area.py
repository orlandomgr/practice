from typing import List
from myUtils.Utils import printResult

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = -10 ** 10
        size = len(points)
        for i in range(size - 2):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i + 1, size - 1):
                x2 = points[j][0]
                y2 = points[j][1]
                for k in range(j + 1, size):
                    x3 = points[k][0]
                    y3 = points[k][1]

                    # print("x1: %s y1: %s x2: %s y2: %s x3: %s y3: %s" %(x1, y1, x2, y2, x3, y3))
                    area = abs(((x1 * y2) + (x2 * y3) + (x3 * y1) - (x1 * y3) - (x2 * y1) - (x3*y2)) / 2)
                    maxArea = max(maxArea, area)
        return maxArea

obj = Solution()

points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
expected = 2.00000
result = obj.largestTriangleArea(points)
printResult(result, expected)

points = [[1,0],[0,0],[0,1]]
expected = 0.50000
result = obj.largestTriangleArea(points)
printResult(result, expected)

points = [[4,6],[6,5],[3,1]]
expected = 5.50000
result = obj.largestTriangleArea(points)
printResult(result, expected)


        # x1y2 + x2y3 + x3y1 - x1y3 - x2y1 - x3y2 
