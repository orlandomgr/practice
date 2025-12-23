from typing import List
from myUtils.Utils import printResult
from collections import deque


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        if not isWater:
            return isWater
        
        rows = len(isWater)
        cols = len(isWater[0])

        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r,c))


        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), ] # right, down, left, up

        while q:
            r, c = q.popleft()
            for dirR, dirC in directions:
                R = r + dirR
                C = c + dirC
                if 0 <= R < rows and 0 <= C < cols and dist[R][C] != 0:
                    if dist[R][C] > dist[r][c] + 1:
                        dist[R][C] = dist[r][c] + 1
                        q.append((R,C))

        return dist


obj = Solution()

isWater = [[0,1],[0,0]]
expected = [[1,0],[2,1]]
result = obj.highestPeak(isWater)
printResult(result, expected)

isWater = [[0,0,1],[1,0,0],[0,0,0]]
expected = [[1,1,0],[0,1,1],[1,2,2]]
result = obj.highestPeak(isWater)
printResult(result, expected)
