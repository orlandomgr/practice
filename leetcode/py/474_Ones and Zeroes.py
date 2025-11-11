from typing import List
from myUtils.Utils import printResult
from collections import Counter
from functools import cache


class Solution:
    # m zero
    # n ones
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counters = [Counter(string) for string in strs]
        @cache
        def dp(position, ones, zeros):
            if position == len(strs):
                return 0

            counter = counters[position]
            new_ones = ones + counter.get("1", 0)
            new_zeros = zeros + counter.get("0", 0)

            return max(
                (
                    (1 + dp(position + 1, new_ones, new_zeros))
                    if new_zeros <= m and new_ones <= n
                    else 0
                ),
                dp(position + 1, ones, zeros),
            )

        return dp(0, 0, 0)


obj = Solution()

strs = ["0", "1", "10", "0001", "111001"]
m = 4
n = 3
expected = 3
result = obj.findMaxForm(strs, m, n)
printResult(result, expected)

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
expected = 4
result = obj.findMaxForm(strs, m, n)
printResult(result, expected)

strs = ["10", "0", "1"]
m = 1
n = 1
expected = 2
result = obj.findMaxForm(strs, m, n)
printResult(result, expected)
