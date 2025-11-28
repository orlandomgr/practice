from typing import List
from myUtils.Utils import printResult

class Solution:
    def intersect_intervals(self, range1_start, range1_end, range2_start, range2_end):
        overlap_start = max(range1_start, range2_start)
        overlap_end = min(range1_end, range2_end)

        if overlap_start <= overlap_end:
            return [overlap_start, overlap_end]
        else:
            return None
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(firstList)
        m = len(secondList)
        if n == 0 or m == 0:
            return res
        firstIdx = 0
        secondIdx = 0

        while firstIdx < n or secondIdx < m:
            # print("first: %s second: %s" %(firstIdx, secondIdx))
            x1, x2 = firstList[firstIdx] if firstIdx < n else firstList[-1]
            y1, y2 = secondList[secondIdx] if secondIdx < m else secondList[-1]

            futureX1,futureX2 = firstList[firstIdx + 1] if firstIdx < n-1 else firstList[-1]
            futureY1,futureY2 = secondList[secondIdx + 1] if secondIdx < m-1 else secondList[-1]

            if x2 >= futureY1:
                # print("futureY1")
                secondIdx += 1
                if secondIdx >= m:
                    firstIdx += 1

            elif y2 >= futureX1:
                # print("futureX1")
                firstIdx += 1
                if firstIdx >= n:
                    secondIdx += 1
            else:
                # print("1: %s, %s 2: %s %s" %(x1, x2, y1, y2))
                if x1 < y1 or x2 < y2:
                    firstIdx += 1
                    if firstIdx >= n:
                        secondIdx += 1
                else: 
                    secondIdx += 1
                    if secondIdx >= m:
                        firstIdx += 1

            overlap = self.intersect_intervals(x1, x2, y1, y2)
            if overlap:
                res.append(overlap)

            if firstIdx >= n and secondIdx >= m:
                break

        return res

obj = Solution()

firstList = [[6,21],[31,32],[43,48],[53,67],[75,95],[96,99]]
secondList = [[8,17],[20,21],[24,40],[47,50],[54,72],[84,85],[91,99]]
expected = [[8,17],[20,21],[31,32],[47,48],[54,67],[84,85],[91,95],[96,99]]
result = obj.intervalIntersection(firstList, secondList)
printResult(result, expected)

firstList = [[0,5],[12,14],[15,18]]
secondList = [[11,15],[18,19]]
expected = [[12,14],[15,15],[18,18]]
result = obj.intervalIntersection(firstList, secondList)
printResult(result, expected)

firstList = [[3,5],[9,20]]
secondList = [[4,5],[7,10],[11,12],[14,15],[16,20]]
expected = [[4,5],[9,10],[11,12],[14,15],[16,20]]
result = obj.intervalIntersection(firstList, secondList)
printResult(result, expected)

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
expected = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
result = obj.intervalIntersection(firstList, secondList)
printResult(result, expected)

firstList = [[1,3],[5,9]]
secondList = []
expected = []
result = obj.intervalIntersection(firstList, secondList)
printResult(result, expected)
