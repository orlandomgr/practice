from typing import List
from myUtils.Utils import printResult
from collections import Counter
import random
import math


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.sum = sum(w)
        self.n = len(self.w)
        for i in range(self.n):
            self.w[i] = self.w[i] / self.sum
        for i in range(1, self.n):
            self.w[i] = self.w[i] + self.w[i - 1]

    def pickIndex(self) -> int:
        if len(self.w) == 1:
            return 0

        N = random.random()

        n = len(self.w)
        left = 0
        right = n

        while left < right:
            mid = (left + right) // 2
            if N < self.w[mid]:
                right = mid
            else:
                left = mid + 1

        return left


w = [3, 14, 1, 7]
obj = Solution(w)
expected = 1
for i in range(10):
    result = obj.pickIndex()
    print(result)
printResult(result, expected)

# w = [1]
# obj = Solution(w)
# expected = 0
# result = obj.pickIndex()
# printResult(result, expected)

# w = [1, 3]
# obj = Solution(w)
# expected = 1, 1, 1, 1, 0
# result = []
# result.append(obj.pickIndex())
# result.append(obj.pickIndex())
# result.append(obj.pickIndex())
# result.append(obj.pickIndex())
# result.append(obj.pickIndex())
# printResult(result, expected)
