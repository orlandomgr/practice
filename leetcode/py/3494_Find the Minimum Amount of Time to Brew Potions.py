from typing import List
from myUtils.Utils import printResult
from functools import cache
import time
from collections import defaultdict, deque
import heapq
import math


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        w = [0] * n
        for m in range(m):
            if m == 0:
                prev = []
                curr = 0
                for s in skill:
                    curr += s * mana[m]
                    prev.append(curr)
            else:
                new = []
                curr = 0
                for s in skill:
                    curr += s * mana[m]
                    new.append(curr)
                nextTime = prev[0]
                for i in range(1, len(prev)):
                    nextTime = max(nextTime, prev[i] - new[i - 1])
                for i in range(len(prev)):
                    prev[i] = new[i] + nextTime
        return prev[-1]


obj = Solution()

skill = [1, 5, 2, 4]
mana = [5, 1, 4, 2]
expected = 110
result = obj.minTime(skill, mana)
printResult(result, expected)

skill = [1,1,1]
mana = [1,1,1]
expected = 5
result = obj.minTime(skill, mana)
printResult(result, expected)

skill = [1,2,3,4]
mana = [1,2]
expected = 21
result = obj.minTime(skill, mana)
printResult(result, expected)
