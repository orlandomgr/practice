from typing import List
from myUtils.Utils import printResult
import heapq
import math 
from itertools import combinations
import heapq
from collections import deque
class Solution:
    # def getNextMove(self, deadends: List[int], target: List[int], lock: List[int]):
    #     n = len(target)
    #     for i in range(n):
    #         if target[i] < lock[i]:


    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"

        if start in deadends:
            return -1
        
        def children(lock):
            result = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                result.append( lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                result.append( lock[:i] + digit + lock[i+1:])
            return result

        q = deque()
        q.append((start, 0))
        visited = set(deadends)

        while q:
            lock, moves = q.popleft()
            if lock == target:
                return moves    
            
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, moves + 1))

        return -1

obj = Solution()

deadends = ["8888"]
target = "0009"
expected = 1
result = obj.openLock(deadends,target)
printResult(result, expected)

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
expected = 6
result = obj.openLock(deadends,target)
printResult(result, expected)

deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
target = "8888"
expected = -1
result = obj.openLock(deadends,target)
printResult(result, expected)
