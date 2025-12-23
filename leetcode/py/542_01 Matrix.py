from typing import List
from myUtils.Utils import printResult
from collections import Counter
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return mat
        
        rows = len(mat)
        cols = len(mat[0])

        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r,c))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), ] # right, down, left, up

        while q:
            r, c = q.popleft()
            for dirR, dirC in directions:
                R = r + dirR
                C = c + dirC
                if 0 <= R < rows and 0 <= C < cols:
                    if dist[R][C] > dist[r][c] + 1:
                        dist[R][C] = dist[r][c] + 1
                        q.append((R,C))

        return dist


obj = Solution()

mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
expected = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
result = obj.updateMatrix(mat)
printResult(result, expected)

mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
expected = [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
result = obj.updateMatrix(mat)
printResult(result, expected)
