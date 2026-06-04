from myUtils.Utils import printResult
from typing import List

"""
You are given two categories of theme park attractions: land rides and water rides.

Land rides
landStartTime[i] – the earliest time the ith land ride can be boarded.
landDuration[i] – how long the ith land ride lasts.
Water rides
waterStartTime[j] – the earliest time the jth water ride can be boarded.
waterDuration[j] – how long the jth water ride lasts.
A tourist must experience exactly one ride from each category, in either order.

A ride may be started at its opening time or any later moment.
If a ride is started at time t, it finishes at time t + duration.
Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.
Return the earliest possible time at which the tourist can finish both rides.
"""

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        finishTime = float('inf')

        for i, land_start in enumerate(landStartTime):
            land_finish = land_start + landDuration[i]
            for j, water_start in enumerate(waterStartTime):
                water_begin = max(water_start, land_finish)
                finishTime = min(finishTime, water_begin + waterDuration[j])

        for j, water_start in enumerate(waterStartTime):
            water_finish = water_start + waterDuration[j]
            for i, land_start in enumerate(landStartTime):
                land_begin = max(land_start, water_finish)
                finishTime = min(finishTime, land_begin + landDuration[i])

        return finishTime



obj = Solution()

landStartTime = [2,8]
landDuration = [4,1]
waterStartTime = [6]
waterDuration = [3]
expected = 9
result = obj.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
printResult(result, expected)

landStartTime = [5]
landDuration = [3]
waterStartTime = [1]
waterDuration = [10]
expected = 14
result = obj.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
printResult(result, expected)

landStartTime = [99]
landDuration = [59]
waterStartTime = [99,54]
waterDuration = [85,20]
expected = 158
result = obj.earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)
printResult(result, expected)


