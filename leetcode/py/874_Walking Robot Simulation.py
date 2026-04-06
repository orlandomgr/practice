from myUtils.Utils import printResult
from typing import List
import math

"""
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot receives an array of integers commands, which represents a sequence of moves that it needs to execute. There are only three possible types of instructions the robot can receive:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, it will stay in its current location (on the block adjacent to the obstacle) and move onto the next command.

Return the maximum squared Euclidean distance that the robot reaches at any point in its path (i.e. if the distance is 5, return 25).

Note:

There can be an obstacle at (0, 0). If this happens, the robot will ignore the obstacle until it has moved off the origin. However, it will be unable to return to (0, 0) due to the obstacle.
North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
"""

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x = 0
        y = 0
        dirs = [(-1,0),(0,1),(1,0),(0,-1)] # left, up, right, down
        currDir = 1
        maxPos = -math.inf
        
        obstacles = {tuple(i) for i in obstacles}
        # print(obstacles)
        for c in commands:
            if c == -1:
                currDir += 1
                if currDir > 3:
                    currDir = 0
                continue
            elif c == -2:
                currDir -= 1
                if currDir < 0:
                    currDir = 3
                continue
            else:
                i = 0
                for i in range(1, c + 1):
                    tmpX = x + i * dirs[currDir][0]
                    tmpY = y + i * dirs[currDir][1]
                    # print(f"c: {c} dirs: {dirs[currDir]} x,y: {tmpX, tmpY}")
                    # print((tmpX, tmpY))
                    if (tmpX, tmpY) in obstacles:
                        i -= 1
                        break

                x += i * dirs[currDir][0]
                y += i * dirs[currDir][1]

                maxPos = max(maxPos, (x * x) + (y * y))

        return maxPos

obj = Solution()

commands = [4,-1,3]
obstacles = []
expected = 25
result = obj.robotSim(commands, obstacles)
printResult(result, expected)

commands = [4,-1,4,-2,4]
obstacles = [[2,4]]
expected = 65
result = obj.robotSim(commands, obstacles)
printResult(result, expected)

commands = [6,-1,-1,6]
obstacles = [[0,0]]
expected = 36
result = obj.robotSim(commands, obstacles)
printResult(result, expected)
