from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        result = 0
        size = len(points)
        for i in range(size):
            y1 = points[i][1]
            maxY = float('-inf')
            for j in range(i+1, size):
                y2 = points[j][1]
                if(y1 >= y2):
                    if(y2 > maxY):
                        result += 1
                        maxY = y2

        return result


obj = Solution()
print(obj.numberOfPairs([[1,1],[2,2],[3,3]]))
print(obj.numberOfPairs([[6,2],[4,4],[2,6]]))
print(obj.numberOfPairs([[3,1],[1,3],[1,1]]))
