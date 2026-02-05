from typing import List

class Solution:
    
    def getNextH(self, height: list[int], idx :int, val: int) -> int:
        # shortArray = height[idx:]
        # end = len(shortArray)
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

        # print(shortArray)
        # maxVal = max(shortArray)
        # maxIdx = shortArray.index(maxVal) + idx
        # print("return index: " + str(maxIdx) + " value: " + str(maxVal))
        # return maxIdx, maxVal

    def getInvalidArea(self, height: list[int], start :int, end: int) -> int:
        # shortArray = height[:start]
        invalid = 0
        for i in range(start, end):
            invalid = invalid + height[i]
        return invalid

    def trap(self, height: List[int]) -> int:
        p1 = 0
        p2 = 0
        area = 0
        # start = 0
        end = len(height)
        i = 0
        while(i < end):
        # for i in range(start, end):
            larea = 0
            h1 = height[i]
            if(h1 <= 0):
                i = i + 1
                continue

            p1 = i
            p2, h2 = self.getNextH(height, i+1, h1)

            # print("values: %s %s " %(h1, h2))
            # print("range: %s %s " %(p1, p2))
            # print("range: " + str(p1) + " " + str(p2))

            larea = larea + min(h1, h2) * ((p2-1) - p1)

            invalidArea = self.getInvalidArea(height, p1 + 1, p2)
            # print("larea: %s invalid: %s" %(larea, invalidArea))
            larea = larea - invalidArea

            area = area + larea
            # print("area: " + str(area))

            i = p2 # + 1
            # print("i: " + str(i))
            if(i > end):
                break

            # i++

        # print("area")
        # print(area)
        return area



obj = Solution()
print(obj.trap([4,2,0,3,2,5])) # 9
print(obj.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6