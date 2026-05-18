from collections import deque
from myUtils.Utils import printResult
from typing import List

"""
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.
"""

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        same_value_positions = {}
        for i, value in enumerate(arr):
            same_value_positions.setdefault(value, []).append(i)

        visited = {0}
        queue = deque([(0, 0)])

        while queue:
            i, steps = queue.popleft()
            if i == n - 1:
                return steps

            next_positions = [i - 1, i + 1] + same_value_positions.get(arr[i], [])
            for j in next_positions:
                if 0 <= j < n and j not in visited:
                    visited.add(j)
                    queue.append((j, steps + 1))

            same_value_positions[arr[i]] = []

        return -1

obj = Solution()

arr = [100,-23,-23,404,100,23,23,23,3,404]
expected = 3
result = obj.minJumps(arr)
printResult(result, expected)

arr = [7]
expected = 0
result = obj.minJumps(arr)
printResult(result, expected)

arr = [7,6,9,6,9,6,9,7]
expected = 1
result = obj.minJumps(arr)
printResult(result, expected)
