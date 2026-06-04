from typing import List
from myUtils.Utils import printResult
import math

"""
You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].
"""

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        result = 0
        n = num1
        def checkNum(num):
            # print(f"cn: {num}")
            sNum = str(num)
            if len(sNum) < 3:
                return 0
            res = 0
            for i in range(len(sNum)-2):
                n1 = int(sNum[i])
                n2 = int(sNum[i+1])
                n3 = int(sNum[i+2])
                # print(f"n1: {n1} n2: {n2} n3: {n3}")
                if (n2 > n1 and n2 > n3) or (n2 < n1 and n2 < n3):
                    res += 1 
            return res
        while n <= num2:
            result += checkNum(n)
            n += 1

        return result

obj = Solution()

num1 = 120
num2 = 130
expected = 3
result = obj.totalWaviness(num1, num2)
printResult(result, expected)

num1 = 198
num2 = 202
expected = 3
result = obj.totalWaviness(num1, num2)
printResult(result, expected)

num1 = 4848
num2 = 4848
expected = 2
result = obj.totalWaviness(num1, num2)
printResult(result, expected)

