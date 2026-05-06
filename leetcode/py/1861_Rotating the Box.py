from typing import List
from myUtils.Utils import printResult
import heapq

"""
You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.
"""
class Solution:    
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)

        def moveItems(row: List[str]):
            cols = len(row)
            if "*" not in row:
                row[0:cols] = sorted(row[0:cols], reverse=True)
            else:
                indices = [i for i, x in enumerate(list(row)) if x == "*"]
                i = 0
                j = i
                while indices:
                    j = indices.pop(0)
                    row[i:j] = sorted(row[i:j], reverse=True)
                    i = j + 1
                i = j + 1
                if i < cols:
                    row[i:cols] = sorted(row[i:cols], reverse=True)
            
        for r in range(n):
            moveItems(boxGrid[r])

        rotated = [list(row) for row in zip(*boxGrid[::-1])]
        # print(rotated)

        return rotated

obj = Solution()

boxGrid = [["*","#","*",".",".",".","#",".","*","."]]
expected = [["*"],["#"],["*"],["."],["."],["."],["."],["#"],["*"],["."]]
result = obj.rotateTheBox(boxGrid)
printResult(result, expected)

boxGrid = [["#",".","#"]]
expected = [["."],
         ["#"],
         ["#"]]
result = obj.rotateTheBox(boxGrid)
printResult(result, expected)

boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
expected = [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
result = obj.rotateTheBox(boxGrid)
printResult(result, expected)

boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
expected = [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
result = obj.rotateTheBox(boxGrid)
printResult(result, expected)
