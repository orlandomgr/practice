from typing import List
from myUtils.Utils import printResult
from functools import cache
from collections import Counter
import queue

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        dPowers = {}
        sortedPower = sorted(power)
        dPowers[0] = 0
        for p in sortedPower:
            if p not in dPowers:
                dPowers[p] = p
            else:
                dPowers[p] += p

        uPowers = list(dPowers.keys())
        dPowers = list(dPowers.values())

        n = len(uPowers)
        dp = [0] * n
        damage = 0
        j = 1
        for i in range(1, n):
            while j < i and uPowers[j] < uPowers[i] - 2:
                damage = max(damage, dp[j])
                j += 1
            dp[i] = damage + dPowers[i]
        return max(dp)

obj = Solution()

power = [7,1,6,3]
expected = 10
result = obj.maximumTotalDamage(power)
printResult(result, expected)

power = [1,1,3,4]
expected = 6
result = obj.maximumTotalDamage(power)
printResult(result, expected)

power = [7,1,6,6]
expected = 13
result = obj.maximumTotalDamage(power)
printResult(result, expected)

