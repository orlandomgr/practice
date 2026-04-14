from typing import List
from myUtils.Utils import printResult

"""
LeetCode 2463. Minimum Total Distance Traveled

The problem asks to minimize the total distance traveled by all robots to be repaired at factories.
Each factory has a capacity limit.

This can be solved using Dynamic Programming.
1. Sort both robots and factories by their positions.
2. Expand each factory's capacity into individual slots. 
   Since total capacity is at most 10,000 (100 factories * 100 limit), this is feasible.
3. Use a DP array where dp[i] is the minimum distance for the first i robots.
"""

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        factory_slots = []
        for pos, limit in factory:
            factory_slots.extend([pos] * limit)

        n = len(robot)
        dp = [0] + [float('inf')] * n
        
        for slot_pos in factory_slots:
            for i in range(n, 0, -1):
                if dp[i-1] != float('inf'):
                    dp[i] = min(dp[i], dp[i-1] + abs(robot[i-1] - slot_pos))
                    
        return dp[n]

if __name__ == "__main__":
    obj = Solution()

    # Example 1
    robot = [0,4,6]
    factory = [[2,2],[6,2]]
    expected = 4
    result = obj.minimumTotalDistance(robot, factory)
    printResult(result, expected)

    # Example 2
    robot = [1,-1]
    factory = [[-2,1],[2,1]]
    expected = 2
    result = obj.minimumTotalDistance(robot, factory)
    printResult(result, expected)
