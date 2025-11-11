from typing import List
from myUtils.Utils import printResult
from functools import cache
import time
from collections import defaultdict, deque
import heapq

class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        if not rains:
            return []
        
        lakes = set()
        indexRain = defaultdict(deque)
        heap = []
        n = len(rains)
        result = [-1] * n

        for day, lake in enumerate(rains):
            indexRain[lake].append(day)

        for day, lake in enumerate(rains):
            if lake == 0:
                if heap:
                    nextDay, toDry = heapq.heappop(heap)
                    lakes.discard(toDry)
                    result[day] = toDry
                else:
                    result[day] = 1
            else:
                if lake in lakes:
                    return []
                lakes.add(lake)

                indexRain[lake].popleft()

                if indexRain[lake]:
                    nextDay = indexRain[lake][0]
                    heapq.heappush(heap, (nextDay, lake))

        # print(indexRain)
        return result

obj = Solution()

rains = [3, 5, 4, 0, 1, 0, 1, 5, 2, 8, 9]
expected = [-1, -1, -1, 5, -1, 1, -1, -1, -1, -1, -1]
result = obj.avoidFlood(rains)
printResult(result, expected)

rains = [1, 0, 2, 0, 2, 1]
expected = [-1, 1, -1, 2, -1, -1]
result = obj.avoidFlood(rains)
printResult(result, expected)

rains = [0, 1, 1]
expected = []
result = obj.avoidFlood(rains)
printResult(result, expected)

rains = [1, 2, 0, 2, 3, 0, 1]
expected = [-1, -1, 2, -1, -1, 1, -1]
result = obj.avoidFlood(rains)
printResult(result, expected)


rains = [1, 1, 0, 0]
expected = []
result = obj.avoidFlood(rains)
printResult(result, expected)

rains = [10, 20, 20]
expected = []
result = obj.avoidFlood(rains)
printResult(result, expected)

rains = [69, 0, 0, 0, 69]
expected = [-1, 69, 1, 1, -1]
result = obj.avoidFlood(rains)
printResult(result, expected)

rains = [1, 2, 3, 4]
expected = [-1, -1, -1, -1]
result = obj.avoidFlood(rains)
printResult(result, expected)

rains = [1, 2, 0, 0, 2, 1]
expected = [-1, -1, 2, 1, -1, -1]
result = obj.avoidFlood(rains)
printResult(result, expected)

rains = [1, 2, 0, 1, 2]
expected = []
result = obj.avoidFlood(rains)
printResult(result, expected)
