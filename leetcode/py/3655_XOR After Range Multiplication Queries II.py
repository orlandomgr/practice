from typing import List
from myUtils.Utils import printResult
"""
You are given an integer array nums of length n and a 2D integer array queries of size q, where queries[i] = [li, ri, ki, vi].

For each query, you must apply the following operations in order:

Set idx = li.
While idx <= ri:
Update: nums[idx] = (nums[idx] * vi) % (109 + 7)
Set idx += ki.
Return the bitwise XOR of all elements in nums after processing all queries.
"""
class Solution:    

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n, B = len(nums), 200 # Threshold for step size k
        
        # 1. Group queries by step size k
        # Large steps (k > B) are rare enough to update directly.
        small_k = [[] for _ in range(B + 1)]
        for l, r, k, v in queries:
            v %= MOD
            if v == 1: continue
            
            if v == 0 or k > B:
                # Brute force for large steps or zeroing (rare cases)
                for i in range(l, r + 1, k):
                    nums[i] = 0 if v == 0 else (nums[i] * v) % MOD
            else:
                small_k[k].append((l, r, v))
        
        # 2. Process small steps efficiently using a difference array
        # This propagates multipliers across the array in O(n) per step size.
        for k in range(1, B + 1):
            if not small_k[k]: continue
            
            # Optimization: If very few queries for this k, update directly
            if len(small_k[k]) < k:
                for l, r, v in small_k[k]:
                    for i in range(l, r + 1, k):
                        nums[i] = (nums[i] * v) % MOD
                continue

            # 'diff' marks where a multiplier starts and where it should be canceled
            diff = [1] * (n + k)
            for l, r, v in small_k[k]:
                diff[l] = (diff[l] * v) % MOD
                last = l + ((r - l) // k) * k
                diff[last + k] = (diff[last + k] * pow(v, MOD - 2, MOD)) % MOD
            
            # Apply multipliers forward by step k and update 'nums'
            for i in range(n):
                if i >= k: 
                    diff[i] = (diff[i] * diff[i - k]) % MOD
                if diff[i] != 1: 
                    nums[i] = (nums[i] * diff[i]) % MOD
                        
        # 3. Compute final XOR result
        ans = 0
        for x in nums: 
            ans ^= x
        return ans
   

obj = Solution()

nums = [1,1,1]
queries = [[0,2,1,4]]
expected = 4
result = obj.xorAfterQueries(nums, queries)
printResult(result, expected)

nums = [2,3,1,5,4]
queries = [[1,4,2,3],[0,2,1,2]]
expected = 31
result = obj.xorAfterQueries(nums, queries)
printResult(result, expected)
