from myUtils.Utils import printResult
from typing import List

"""
You are given an integer side, representing the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.

You are also given a positive integer k and a 2D integer array points, where points[i] = [xi, yi] represents the coordinate of a point lying on the boundary of the square.

You need to select k elements among points such that the minimum Manhattan distance between any two points is maximized.

Return the maximum possible minimum Manhattan distance between the selected k points.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.
"""

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def get_pos(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y
                
        positions = sorted([get_pos(x, y) for x, y in points])
        num_points = len(positions)
        perimeter = 4 * side
        extended_positions = positions + [p + perimeter for p in positions]
        
        def check(min_dist):
            next_point_idx = [2 * num_points] * (2 * num_points)
            j = 0
            for i in range(2 * num_points):
                while j < 2 * num_points and extended_positions[j] - extended_positions[i] < min_dist:
                    j += 1
                next_point_idx[i] = j
                
            search_limit = min(num_points, next_point_idx[0])
            for i in range(search_limit):
                curr = i
                for _ in range(k - 1):
                    curr = next_point_idx[curr]
                    if curr == 2 * num_points:
                        break
                else:
                    if extended_positions[curr] <= extended_positions[i] + perimeter - min_dist:
                        return True
            return False

        low = 1
        high = perimeter // k
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return result

obj = Solution()

side = 2
points = [[0,2],[2,0],[2,2],[0,0]]
k = 4
expected = 2
result = obj.maxDistance(side, points, k)
printResult(result, expected)

side = 2
points = [[0,0],[1,2],[2,0],[2,2],[2,1]]
k = 4
expected = 1
result = obj.maxDistance(side, points, k)
printResult(result, expected)

side = 2
points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]]
k = 5
expected = 1
result = obj.maxDistance(side, points, k)
printResult(result, expected)
