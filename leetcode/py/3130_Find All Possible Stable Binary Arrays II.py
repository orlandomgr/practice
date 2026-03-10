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

        # prefix sums to speed up run-word calculations:
        # sum1_i[i][j] = sum(dp[k][j][1] for k in [0..i])
        # sum0_j[i][j] = sum(dp[i][k][0] for k in [0..j])
        sum1_i = [[0] * (one + 1) for _ in range(zero + 1)]
        sum0_j = [[0] * (one + 1) for _ in range(zero + 1)]

        # iterate through all possible counts of zeros/ones
        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 and j == 0:
                    # no bits used yet
                    continue

                # compute sequences ending in 0 using a run of up to `limit` zeros
                if i > 0:
                    maxrun = min(limit, i)
                    # we need sum of dp[i-r][j][1] for r=1..maxrun
                    # this is sum1_i[i-1][j] - sum1_i[i-maxrun-1][j]
                    end = sum1_i[i-1][j]
                    start = sum1_i[i-maxrun-1][j] if i-maxrun-1 >= 0 else 0
                    total0 = end - start
                    # special case: when j==0 we should add 1 if the entire
                    # run of `i` zeros is allowed (i<=limit), but the formula
                    # already sets dp[0][0][1]==0 so we add it explicitly
                    if j == 0 and i <= limit:
                        total0 += 1
                    dp[i][j][0] = total0 % mod

                # compute sequences ending in 1 using a run of up to `limit` ones
                if j > 0:
                    maxrun = min(limit, j)
                    end = sum0_j[i][j-1]
                    start = sum0_j[i][j-maxrun-1] if j-maxrun-1 >= 0 else 0
                    total1 = end - start
                    if i == 0 and j <= limit:
                        total1 += 1
                    dp[i][j][1] = total1 % mod

                # update prefix sums after current dp cell is known
                sum1_i[i][j] = (dp[i][j][1] + (sum1_i[i-1][j] if i > 0 else 0)) % mod
                sum0_j[i][j] = (dp[i][j][0] + (sum0_j[i][j-1] if j > 0 else 0)) % mod

        return (dp[zero][one][0] + dp[zero][one][1]) % mod


obj = Solution()

zero = 142
one = 768
limit = 418
expected = 549356871
result = obj.numberOfStableArrays(zero, one, limit)
printResult(result, expected)

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
