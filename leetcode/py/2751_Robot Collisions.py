from typing import List
from myUtils.Utils import printResult
import heapq

"""
There are n 1-indexed robots, each having a position on a line, health, and movement direction.

You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i] is either 'L' for left or 'R' for right). All integers in positions are unique.

All robots start moving on the line simultaneously at the same speed in their given directions. If two robots ever share the same position while moving, they will collide.

If two robots collide, the robot with lower health is removed from the line, and the health of the other robot decreases by one. The surviving robot continues in the same direction it was going. If both robots have the same health, they are both removed from the line.

Your task is to determine the health of the robots that survive the collisions, in the same order that the robots were given, i.e. final health of robot 1 (if survived), final health of robot 2 (if survived), and so on. If there are no survivors, return an empty array.

Return an array containing the health of the remaining robots (in the order they were given in the input), after no further collisions can occur.

Note: The positions may be unsorted.

"""

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        oneway = set(list(directions))
        if len(oneway) == 1:
            return healths

        posMap = {p: i for i, p in enumerate(positions)}
        stack = []
        for p in sorted(positions):
            i = posMap[p]

            if directions[i] == "R":
                stack.append(i)
            else:
                while stack and healths[i]:
                    j = stack.pop()
                    if healths[i] > healths[j]:
                        healths[j] = 0
                        healths[i] -= 1
                    elif healths[i] < healths[j]:
                        healths[i] = 0
                        healths[j] -= 1
                    else:
                        healths[i] = healths[j] = 0
                    if healths[j] > 0:
                        stack.append(j)


        return [h for h in healths if h > 0]
    
obj = Solution()


positions = [12,33,37]
healths = [49,5,38]
directions = "RLL"
expected = [47]
result = obj.survivedRobotsHealths(positions, healths, directions)
printResult(result, expected)


positions = [5,4,3,2,1]
healths = [2,17,9,15,10]
directions = "RRRRR"
expected = [2,17,9,15,10]
result = obj.survivedRobotsHealths(positions, healths, directions)
printResult(result, expected)

positions = [3,5,2,6]
healths = [10,10,15,12]
directions = "RLRL"
expected = [14]
result = obj.survivedRobotsHealths(positions, healths, directions)
printResult(result, expected)

positions = [1,2,5,6]
healths = [10,10,11,11]
directions = "RLRL"
expected = []
result = obj.survivedRobotsHealths(positions, healths, directions)
printResult(result, expected)
