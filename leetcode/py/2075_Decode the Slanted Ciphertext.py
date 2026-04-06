from myUtils.Utils import printResult
from typing import List

"""
There is an endless straight line populated with some robots and walls. You are given integer arrays robots, distance, and walls:
robots[i] is the position of the ith robot.
distance[i] is the maximum distance the ith robot's bullet can travel.
walls[j] is the position of the jth wall.
Every robot has one bullet that can either fire to the left or the right at most distance[i] meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it immediately stops at that robot and cannot continue.

Return the maximum number of unique walls that can be destroyed by the robots.

Notes:

A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.
Robots are not destroyed by bullets.
"""
from typing import List
from collections import defaultdict
import bisect

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = rows
        m = len(encodedText) // rows
        data = []
        i = 0
        while i < len(encodedText):
            data.append(encodedText[i:i+m])
            i += m

        def getDiagonalData(row, col):
            result = []
            r = row
            c = col
            while c < m and r < n:
                result.append(data[r][c])
                r += 1
                c += 1
            return "".join(result)

        result = []
        limit = m - 1 if rows > 1 else m
        for c in range(m):
                result.append(getDiagonalData(0, c))

        # print(data)
        # print("".join(result))
        return "".join(result).rstrip()

obj = Solution()

encodedText = " b  ac"
rows = 2
expected = " abc"
result = obj.decodeCiphertext(encodedText, rows)
printResult(result, expected)

encodedText = "ch   ie   pr"
rows = 3
expected = "cipher"
result = obj.decodeCiphertext(encodedText, rows)
printResult(result, expected)

encodedText = "iveo    eed   l te   olc"
rows = 4
expected = "i love leetcode"
result = obj.decodeCiphertext(encodedText, rows)
printResult(result, expected)

encodedText = "coding"
rows = 1
expected = "coding"
result = obj.decodeCiphertext(encodedText, rows)
printResult(result, expected)

