from typing import List
from myUtils.Utils import printResult

class Solution:
    
    def getNextH(self, height: List[int], idx :int, val: int) -> int:
        end = len(height)
        maxPrevIdx = idx
        maxPrevVal = 0
        for i in range(idx, end):
            if(maxPrevVal < height[i]):
                maxPrevIdx = i
                maxPrevVal = height[i]
            if(height[i] >= val):
                return i, height[i]

        # print("return index: %s value: %s idx: %s val: %s" %(maxPrevIdx, maxPrevVal, idx, val))

        return maxPrevIdx, maxPrevVal

    def getInvalidArea(self, height: list[int], start :int, end: int) -> int:
        invalid = 0
        for i in range(start, end):
            invalid = invalid + height[i]
        return invalid

    def trap(self, height: list[int]) -> int:
        p1 = 0
        p2 = 0
        area = 0
        end = len(height)
        i = 0
        while(i < end):
            larea = 0
            h1 = height[i]
            if(h1 <= 0):
                i = i + 1
                continue

            p1 = i
            p2, h2 = self.getNextH(height, i+1, h1)

            larea = larea + min(h1, h2) * ((p2-1) - p1)

            invalidArea = self.getInvalidArea(height, p1 + 1, p2)
            larea = larea - invalidArea

            area = area + larea

            i = p2 
            if(i > end):
                break
        return area
    
obj = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
expected = 6
result = obj.trap(height)
printResult(result, expected)    

height = [4,2,0,3,2,5]
expected = 9
result = obj.trap(height)
printResult(result, expected)    