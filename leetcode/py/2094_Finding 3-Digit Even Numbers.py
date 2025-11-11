from typing import List
from myUtils.Utils import printResult
from functools import cache
import itertools
import heapq
from collections import deque


class Solution:

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = {}
        size = len(digits)
        for i in range(size):
            if digits[i] == 0:
                continue
            valI = digits[i] * 100
            for j in range(size):
                if i == j:
                    continue
                valJ = digits[j] * 10
                for k in range(size):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    result[valI + valJ + digits[k]] = 1
        result = list(result.keys())
        result.sort()
        return result

        # i = 0
        # while i < size:

        # for i in range(size):

        # comb = itertools.permutations(digits, 3)
        # result = {}
        # for a,b,c in comb:
        #     if a == 0:
        #         continue
        #     if c % 2 != 0:
        #         continue
        #     result[int(str(a) + str(b) + str(c))] = 1

        # result = list(result.keys())
        # result.sort()
        # return result


obj = Solution()

digits = [2, 1, 3, 0]
expected = [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
result = obj.findEvenNumbers(digits)
printResult(result, expected)

digits = [2, 2, 8, 8, 2]
expected = [222, 228, 282, 288, 822, 828, 882]
result = obj.findEvenNumbers(digits)
printResult(result, expected)

digits = [3, 7, 5]
expected = []
result = obj.findEvenNumbers(digits)
printResult(result, expected)
