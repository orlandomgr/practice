from typing import List
from myUtils.Utils import printResult


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        matching = []
        for x1, y1 in points:
            if x1 == x or y1 == y:
                dist = abs(x - x1) + abs(y - y1)
                matching.append((dist, x1, y1))

        matching.sort()        
        candidate = -1
        res = 10**10
        if matching:
            val = matching[0][0]
            for v, x1, y1 in matching:
                if v == val:
                    res = min(res, points.index([x1,y1]))
            candidate = res
        return candidate


obj = Solution()

x = 3
y = 4
points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
expected = 2
result = obj.nearestValidPoint(x, y, points)
printResult(result, expected)

x = 3
y = 4
points = [[3, 4]]
expected = 0
result = obj.nearestValidPoint(x, y, points)
printResult(result, expected)

x = 3
y = 4
points = [[2, 3]]
expected = -1
result = obj.nearestValidPoint(x, y, points)
printResult(result, expected)
