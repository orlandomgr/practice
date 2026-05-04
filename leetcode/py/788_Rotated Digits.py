from typing import List
from myUtils.Utils import printResult

"""
An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. For example:

0, 1, and 8 rotate to themselves,
2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
6 and 9 rotate to each other, and
the rest of the numbers do not rotate to any other number and become invalid.
Given an integer n, return the number of good integers in the range [1, n].
"""
# 0 rotates to 0
# 1 rotates to 1
# 8 rotates to 8

# 2 rotates to 5
# 5 rotates to 2
# 6 rotates to 9
# 9 rotates to 6


class Solution:
    def rotatedDigits(self, n: int) -> int:
        result = 0
        rotations = {
            0:0,
            1:1,
            8:8,
            2:5,
            5:2,
            6:9,
            9:6
        }
        invalid = [
            "3",
            "4",
            "7"
        ]
        def rotate(n):
            if n == 0:
                return 0
            digits = []
            # print(f"rotate: {n}")
            while n > 0:
                num = n % 10
                # print(num)
                digits.append(rotations[num])
                n //= 10
            digits.reverse()
            # print(digits)
            return int("".join(map(str, digits)))


        for i in range(1, n+1):
            s = str(i)
            hasInvalid = any(word in s for word in invalid)
            # print(f"s: {s} hasInvalid: {hasInvalid}")
            if hasInvalid:
                continue

            if i != rotate(i):
                result += 1

        return result

obj = Solution()

n = 13
expected = 5
result = obj.rotatedDigits(n)
printResult(result, expected)

n = 10
expected = 4
result = obj.rotatedDigits(n)
printResult(result, expected)

n = 1
expected = 0
result = obj.rotatedDigits(n)
printResult(result, expected)

n = 2
expected = 1
result = obj.rotatedDigits(n)
printResult(result, expected)

n = 857
expected = 247
result = obj.rotatedDigits(n)
printResult(result, expected)
