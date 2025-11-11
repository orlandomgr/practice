from typing import List
from myUtils.Utils import printResult
from functools import cache
from collections import Counter
import queue
import math


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7

        @cache
        def aux(remaining, k_needed, index, carry):
            if remaining < 0 or k_needed < 0 or remaining + carry.bit_count() < k_needed:
                return 0
            if remaining == 0:
                return 1 if k_needed == carry.bit_count() else 0
            if index >= n:
                return 0

            result = 0
            for i in range(remaining + 1):
                tmp = math.comb(remaining, i) * pow(nums[index], i, MOD) % MOD
                newCarry = carry + i 
                result += tmp * aux(remaining - i, k_needed - (newCarry % 2), index + 1, newCarry // 2)
                result %= MOD
            return result

        return aux(m, k, 0, 0)


obj = Solution()
m = 5
k = 5
nums = [1, 10, 100, 10000, 1000000]
expected = 991600007
result = obj.magicalSum(m, k, nums)
printResult(result, expected)

obj = Solution()
m = 2
k = 2
nums = [5, 4, 3, 2, 1]
expected = 170
result = obj.magicalSum(m, k, nums)
printResult(result, expected)

obj = Solution()
m = 1
k = 1
nums = [28]
expected = 28
result = obj.magicalSum(m, k, nums)
printResult(result, expected)
