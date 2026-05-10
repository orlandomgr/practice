from myUtils.Utils import printResult
from typing import List
import math 
from collections import deque, defaultdict

"""
You are given an integer array nums of length n.

You start at index 0, and your goal is to reach index n - 1.

From any index i, you may perform one of the following operations:

Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
Return the minimum number of jumps required to reach index n - 1.
"""

class Solution:
    def get_prime_factors(self, n):
        factors = set()
        d = 2
        temp = n
        while d * d <= temp:
            if temp % d == 0:
                factors.add(d)
                while temp % d == 0:
                    temp //= d
            d += 1
        if temp > 1:
            factors.add(temp)
        return factors

    def is_prime(self, n):
        if n < 2: return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0: return False
        return True

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return 0

        prime_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            d = 2
            temp = val
            while d * d <= temp:
                if temp % d == 0:
                    prime_to_indices[d].append(i)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                prime_to_indices[temp].append(i)

        queue = deque([(0, 0)])
        visited_idx = {0}
        visited_primes = set() 

        while queue:
            curr_idx, dist = queue.popleft()

            if curr_idx == n - 1:
                return dist

            for neighbor in [curr_idx - 1, curr_idx + 1]:
                if 0 <= neighbor < n and neighbor not in visited_idx:
                    visited_idx.add(neighbor)
                    queue.append((neighbor, dist + 1))

            val = nums[curr_idx]
            if self.is_prime(val):
                if val not in visited_primes:
                    for target_idx in prime_to_indices[val]:
                        if target_idx not in visited_idx:
                            visited_idx.add(target_idx)
                            queue.append((target_idx, dist + 1))
                    visited_primes.add(val)

        return -1



obj = Solution()

nums = [1,2,4,6]
expected = 2
result = obj.minJumps(nums)
printResult(result, expected)

nums = [2,3,4,7,9]
expected = 2
result = obj.minJumps(nums)
printResult(result, expected)

nums = [4,6,5,8]
expected = 3
result = obj.minJumps(nums)
printResult(result, expected)
