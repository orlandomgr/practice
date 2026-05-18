from typing import List
from myUtils.Utils import printResult

"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        stack = []

        visited = {}

        stack.append(start)
        while stack:
            idx = stack.pop()
            if 0 <= idx < n:
                if arr[idx] == 0:
                    return True
                if idx in visited:
                    continue
                visited[idx] = 1
                stack.append(idx + arr[idx])
                stack.append(idx - arr[idx])

        return False


obj = Solution()

arr = [4,2,3,0,3,1,2]
start = 5
expected = True
result = obj.canReach(arr, start)
printResult(result, expected)

arr = [4,2,3,0,3,1,2]
start = 0
expected = True
result = obj.canReach(arr, start)
printResult(result, expected)

arr = [3,0,2,1,2]
start = 2
expected = False
result = obj.canReach(arr, start)
printResult(result, expected)

