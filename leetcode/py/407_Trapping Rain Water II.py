from typing import List
from myUtils.Utils import printResult
from functools import cache

class Solution:
    # def getMinHeight(self, heightMap: List[List[int]])
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        result = 0
        n = len(heightMap)
        m = len(heightMap[0])
        if n < 3:
            return result

        minHeight = 10 ** 10
        water = 0
        for i in range(1, m-1):
            minHeight = min(minHeight, heightMap[0][i]) 
            minHeight = min(minHeight, heightMap[n-1][i]) 

        for i in range(1, n-1):
            minHeight = min(minHeight, heightMap[i][0]) 
            minHeight = min(minHeight, heightMap[i][m-1]) 
        print(minHeight)

        for i in range(1, n-1):
            for j in range(1, m-1):
                water += abs(minHeight - heightMap[i][j])

        return water
        
obj = Solution()

heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4]]
expected = 0
result = obj.trapRainWater(heightMap)
printResult(result,expected)

heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
expected = 4
result = obj.trapRainWater(heightMap)
printResult(result,expected)

heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
expected = 10
result = obj.trapRainWater(heightMap)
printResult(result,expected)


[ 
    1,  3,  2,
    4,  2,  3,
    3,  1,  3,
    1,  3,  2,
    3,  2,  3,
    2,  4,  1,
],

[
    3,  3,  3,  3,  3,
    3,  2,  2,  2,  3,
    3,  2,  1,  2,  3,
    3,  2,  2,  2,  3,
    3,  3,  3,  3,  3,
],
