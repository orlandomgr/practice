from typing import List
from myUtils.Utils import printResult
from functools import cache
from collections import deque
import queue


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        result = -10**10
        n = len(energy)

        for i in range(n - k, n):
            tmpSum = 0
            j = i 
            while j >= 0:
               tmpSum += energy[j]
               result = max(result, tmpSum)
               j -= k

            # print(result)
        return result


obj = Solution()

energy = [5,-10,4,3,5,-9,9,-7]
k = 2
expected = 23
result = obj.maximumEnergy(energy, k)
printResult(result, expected)

energy = [5, 2, -10, -5, 1]
k = 3
expected = 3
result = obj.maximumEnergy(energy, k)
printResult(result, expected)

energy = [-2, -3, -1]
k = 2
expected = -1
result = obj.maximumEnergy(energy, k)
printResult(result, expected)
