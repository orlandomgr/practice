from typing import List
from myUtils.Utils import printResult
from functools import cache
import time
from collections import defaultdict, deque
import heapq
import math 

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        potions.sort()
        potionsSize = len(potions)

        for s in spells:
            left = 0
            right = potionsSize - 1

            while left <= right:
                mid = (left + right) // 2
                if s * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            result.append(potionsSize - left)
        return result
    

obj = Solution()

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7
expected = [4,0,3]
result = obj.successfulPairs(spells, potions, success)
printResult(result, expected)

spells = [3,1,2]
potions = [8,5,8]
success = 16
expected = [2,0,2]
result = obj.successfulPairs(spells, potions, success)
printResult(result, expected)
