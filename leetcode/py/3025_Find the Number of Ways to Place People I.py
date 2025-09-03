from typing import List

class Solution:
    # def checkRectangle(x1, y1, x2, y2, points) -> bool:
    #     for idx, point in enumerate(points):
    #         isInX = x1 <= point[0] <= x2
    #         isInY = y1 <= point[1] <= y2
    #         if (isInX and isInY):
    #             return False
    #     return True

    # def checkPair(x1, y1, points) -> int:
    #     result = 0

    def numberOfPairs(self, points: List[List[int]]) -> int:
        result = 0
        size = len(points)
        for i in range(size):
            x1 = points[i][0]
            y1 = points[i][1]
            # print("x1: %s y1: %s" %(x1, y1))
            for j in range(size):
                x2 = points[j][0]
                y2 = points[j][1]
                if i == j or (x1 > x2 or y1 < y2):
                    continue

                # print("x2: %s y2: %s" %(x2, y2))
                inside = False
                for k in range(size):
                    if i == k or j == k:
                        continue

                    x3 = points[k][0]
                    y3 = points[k][1]
                    # print("x3: %s y3: %s" %(x3, y3))
                    if x1 <= x3 <= x2 and y2 <= y3 <= y1:
                        inside = True
                        break

                if inside == False:
                    result += 1

        return result


obj = Solution()
print(obj.numberOfPairs([[1,1],[2,2],[3,3]]))
print(obj.numberOfPairs([[6,2],[4,4],[2,6]]))
print(obj.numberOfPairs([[3,1],[1,3],[1,1]]))
