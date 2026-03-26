from typing import List
from myUtils.Utils import printResult

"""
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
If a cell is discounted, the rest of the section must remain connected.
Return true if such a partition exists; otherwise, return false.

Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.
"""
class Solution:    

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        def transpose(grid):
            return list(zip(*grid))

        def isValidRemoval(grid, i, x, row_sets):
            return (i > 0 or x == grid[i][0] or x == grid[i][-1]) and \
                   (len(grid[0]) > 1 or x in row_sets[-1] or x in row_sets[0])
        
        def check(grid):
            row_totals = [0] * len(grid)
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    row_totals[i] += grid[i][j]
            total = sum(row_totals)
                
            curr = 0
            seen = set()
            row_sets = []
            for i in range(len(grid)):
                curr += row_totals[i]
                seen.update(grid[i])
                row_sets.append(set(grid[i]))
                if curr > 0 and curr*2 == total:
                    return True
                elif curr*2 - total in seen and isValidRemoval(grid, i, curr*2 - total, row_sets):
                    return True
                # elif curr * 2 > total:
                #     break
            return False
            
        return check(grid) or check(transpose(grid)) or check(list(reversed(grid))) or check(list(reversed(transpose(grid))))

        # return check(grid) or check(transpose(grid)) or check(list(reversed(grid))) or check(list(reversed(transpose(grid))))
        # return check(grid) or check(list(reversed(grid))) or check(list(reversed(transpose(grid))))


obj = Solution()

grid = [[253,10,10]]
expected = True
result = obj.canPartitionGrid(grid)
printResult(result, expected)

grid = [[54756,54756]]
expected = True
result = obj.canPartitionGrid(grid)
printResult(result, expected)

grid = [[1,4],[2,3]]
expected = True
result = obj.canPartitionGrid(grid)
printResult(result, expected)

grid = [[1,3],[2,4]]
expected = True
result = obj.canPartitionGrid(grid)
printResult(result, expected)

grid = [[1,2,4],[2,3,5]]
expected = False
result = obj.canPartitionGrid(grid)
printResult(result, expected)

grid = [[4,1,8],[3,2,6]]
expected = False
result = obj.canPartitionGrid(grid)
printResult(result, expected)

grid = [[1,2],[3,4]]
expected = True
result = obj.canPartitionGrid(grid)
printResult(result, expected)
