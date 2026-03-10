from typing import List
from myUtils.Utils import printResult

"""
You are given 3 positive integers zero, one, and limit.

A binary array arr is called stable if:

The number of occurrences of 0 in arr is exactly zero.
The number of occurrences of 1 in arr is exactly one.
Each subarray of arr with a size greater than limit must contain both 0 and 1.
Return the total number of stable binary arrays.

Since the answer may be very large, return it modulo 10^9 + 7.
"""
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # trivial cases: empty array or only one type of bit
        if zero == 0 and one == 0:
            return 1
        if zero == 0:
            return 1 if one <= limit else 0
        if one == 0:
            return 1 if zero <= limit else 0

        dp = [[[0,0] for _ in range(one + 1)] for _ in range(zero + 1)]
        mod = ((10 ** 9) + 7)

        # iterate through all possible counts of zeros/ones
        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 and j == 0:
                    continue

                # compute sequences ending in 0 using a run of r zeros
                if i > 0:
                    total0 = 0
                    maxrun = min(limit, i)
                    for r in range(1, maxrun + 1):
                        if j > 0:
                            total0 += dp[i-r][j][1]
                        else:
                            # no ones to worry about; only valid if the run covers all zeros
                            if r == i:
                                total0 += 1
                    dp[i][j][0] = total0 % mod

                # compute sequences ending in 1 using a run of r ones
                if j > 0:
                    total1 = 0
                    maxrun = min(limit, j)
                    for r in range(1, maxrun + 1):
                        if i > 0:
                            total1 += dp[i][j-r][0]
                        else:
                            if r == j:
                                total1 += 1
                    dp[i][j][1] = total1 % mod

        return (dp[zero][one][0] + dp[zero][one][1]) % mod


obj = Solution()

zero = 1
one = 1
limit = 2
expected = 2
result = obj.numberOfStableArrays(zero, one, limit)
printResult(result, expected)

zero = 1
one = 2
limit = 1
expected = 1
result = obj.numberOfStableArrays(zero, one, limit)
printResult(result, expected)

zero = 3
one = 3
limit = 2
expected = 14
result = obj.numberOfStableArrays(zero, one, limit)
printResult(result, expected)
