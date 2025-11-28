from myUtils.Utils import printResult
from typing import List
from collections import deque


class Solution:
    def getStartingPoints(self, rooms: List[List[int]]):
        n = len(rooms)
        m = len(rooms[0])
        positions = []
        for r in range(n):
            for c in range(m):
                if rooms[r][c] == 0:
                    positions.append((r,c,0))
        return positions

    def navigate(self, rooms: List[List[int]], starting):
        n = len(rooms)
        m = len(rooms[0])
        q = deque(starting)
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # left, right, up, down
        while q:
            r,c,cost = q.popleft()
            if rooms[r][c] == -1:
                continue
            if rooms[r][c] != 0 and rooms[r][c] != -1:
                if rooms[r][c] < cost:
                    continue
                rooms[r][c] = cost
            for dirR, dirC in directions:
                R, C = r + dirR, c + dirC
                if 0 <= R < n and 0 <= C < m and rooms[R][C] != 0 and rooms[R][C] != -1:
                    q.append((R,C,cost+1))

        return rooms

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        starting = self.getStartingPoints(rooms)
        rooms = self.navigate(rooms, starting)
        # print(rooms)
        return rooms



obj = Solution()

rooms = [[0,0],[0,0]]
expected= [[0,0],[0,0]]
result = obj.wallsAndGates(rooms)
printResult(result, expected)        

rooms = [
    [2147483647, -1, 0,21474836471],
    [2147483647, 2147483647, 2147483647, -1], 
    [2147483647, -1, 2147483647, -1],
    [0, -1,2147483647, 214748364711]
]
expected= [[3, -1,0,1], [2,2,1,-1], [1, -1,2, -1], [0, -1,3,4]]
result = obj.wallsAndGates(rooms)
printResult(result, expected)        


rooms = [[-1]]
expected= [[-1]]
result = obj.wallsAndGates(rooms)
printResult(result, expected)        

