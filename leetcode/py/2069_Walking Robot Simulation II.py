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

class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.maxDist = (width * 2) + (height * 2) - 4 
        self.dirs = [(0,-1),(1,0),(0,1),(-1,0)]
        self.dirsStr = ["South", "East", "North", "West"]
        self.dir = 1
        self.x = 0
        self.y = 0

    def step(self, num: int) -> None:
        if num == 0: return
        
        if self.x == 0 and self.y == 0 and self.dir == 1:
            if num % self.maxDist == 0:
                self.dir = 0
        
        num %= self.maxDist
        if num == 0: return

        while num > 0:
            dx, dy = self.dirs[self.dir]
            
            if dx == 1:   
                dist = self.width - 1 - self.x
            elif dx == -1: 
                dist = self.x
            elif dy == 1:  
                dist = self.height - 1 - self.y
            else:          
                dist = self.y
            
            if dist >= num:
                self.x += num * dx
                self.y += num * dy
                num = 0
            else:
                self.x += dist * dx
                self.y += dist * dy
                num -= dist
                self.dir = (self.dir + 1) % 4

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.dirsStr[self.dir]


# Your Robot object will be instantiated and called as such:

obj = Robot(6, 3)
obj.step(2)
obj.step(2)
result = obj.getPos()
printResult(result, [4, 0])
result = obj.getDir()
printResult(result, "East")
obj.step(2)
obj.step(1)
obj.step(4)
result = obj.getPos()
printResult(result, [1, 2])
result = obj.getDir()
printResult(result, "West")
