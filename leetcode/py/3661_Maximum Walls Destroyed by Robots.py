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
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        if not robots:
            return 0

        # Group robots by position and get top 2 distances for each position
        pos_to_dists = defaultdict(list)
        for r, d in zip(robots, distance):
            pos_to_dists[r].append(d)

        sorted_pos = sorted(pos_to_dists.keys())
        m = len(sorted_pos)

        # Identify walls at robot positions (these are always destroyed)
        walls.sort()
        robot_pos_set = set(sorted_pos)

        walls_at_robots = 0
        other_walls = []
        for w in walls:
            if w in robot_pos_set:
                walls_at_robots += 1
            else:
                other_walls.append(w)

        # Partition other walls into gaps between robots
        # Gaps: gaps[0] is walls < sorted_pos[0], gaps[j] is walls between sorted_pos[j-1] and sorted_pos[j]
        gaps = [[] for _ in range(m + 1)]
        for w in other_walls:
            idx = bisect.bisect_right(sorted_pos, w)
            gaps[idx].append(w)

        robot_options = []
        for p in sorted_pos:
            dists = sorted(pos_to_dists[p], reverse=True)
            if len(dists) == 1:
                # One robot: can fire left (d1) OR right (d1)
                robot_options.append([(dists[0], 0), (0, dists[0])])
            else:
                # Multiple robots: best to use top 2 distances for left and right
                robot_options.append([(dists[0], dists[1]), (dists[1], dists[0])])

        # DP initialization: walls in the first gap (left of the first robot)
        dp = {}
        p1 = sorted_pos[0]
        for idx, (dL, dR) in enumerate(robot_options[0]):
            count = 0
            for w in gaps[0]:
                if w >= p1 - dL:
                    count += 1
            dp[idx] = count

        # DP transitions for gaps between adjacent robots
        for j in range(1, m):
            new_dp = defaultdict(lambda: -1)
            pj = sorted_pos[j]
            pj_prev = sorted_pos[j-1]
            gap_walls = gaps[j]

            for curr_idx, (dL_curr, dR_curr) in enumerate(robot_options[j]):
                for prev_idx, (dL_prev, dR_prev) in enumerate(robot_options[j-1]):
                    if dp[prev_idx] == -1: continue

                    count = 0
                    for w in gap_walls:
                        if w <= pj_prev + dR_prev or w >= pj - dL_curr:
                            count += 1

                    if dp[prev_idx] + count > new_dp[curr_idx]:
                        new_dp[curr_idx] = dp[prev_idx] + count
            dp = new_dp

        # Final gap: walls to the right of the last robot
        ans = 0
        pm = sorted_pos[m-1]
        for idx, (dL, dR) in enumerate(robot_options[m-1]):
            if dp[idx] == -1: continue
            count = 0
            for w in gaps[m]:
                if w <= pm + dR:
                    count += 1
            if dp[idx] + count > ans:
                ans = dp[idx] + count

        return ans + walls_at_robots

obj = Solution()

robots = [63,56,40,45,4,9,44,69,55,26,73,15,12,60,43,39,37,74,36,34,13,23,66,14,11,42,72,3,57,10,53,8,70,17,58,61,30,32]
distance = [8,7,4,8,9,5,2,4,5,2,6,9,5,9,5,3,7,6,9,2,8,7,4,3,5,1,7,5,1,3,5,3,5,4,8,7,6,4]
walls = [6,22,50,52,20,9,23,75,26,21,60,58,41,28,30]
expected = 15
result = obj.maxWalls(robots, distance, walls)
printResult(result, expected)

robots = [17,59,32,11,72,18]
distance = [5,7,6,5,2,10]
walls = [17,25,33,29,54,53,18,35,39,37,20,14,34,13,16,58,22,51,56,27,10,15,12,23,45,43,21,2,42,7,32,40,8,9,1,5,55,30,38,4,3,31,36,41,57,28,11,49,26,19,50,52,6,47,46,44,24,48]
expected = 37
result = obj.maxWalls(robots, distance, walls)
printResult(result, expected)

robots = [4]
distance = [3]
walls = [1,10]
expected = 1
result = obj.maxWalls(robots, distance, walls)
printResult(result, expected)

robots = [10,2]
distance = [5,1]
walls = [5,2,7]
expected = 3
result = obj.maxWalls(robots, distance, walls)
printResult(result, expected)

robots = [1,2]
distance = [100,1]
walls = [10]
expected = 0
result = obj.maxWalls(robots, distance, walls)
printResult(result, expected)

