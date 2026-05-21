from typing import List
from myUtils.Utils import printResult

"""
You are given two 0-indexed integer permutations A and B of length n.

A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

Return the prefix common array of A and B.

A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
"""
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        seen_a = set()
        seen_b = set()
        common_count = 0
        
        for i in range(len(A)):
            if A[i] in seen_b:
                common_count += 1
            seen_a.add(A[i])
            
            if B[i] in seen_a:
                common_count += 1
            seen_b.add(B[i])
            
            result.append(common_count)
        
        return result


obj = Solution()

A = [1,3,2,4]
B = [3,1,2,4]
expected = [0,2,3,4]
result = obj.findThePrefixCommonArray(A, B)
printResult(result, expected)

A = [2,3,1]
B = [3,1,2]
expected = [0,1,3]
result = obj.findThePrefixCommonArray(A, B)
printResult(result, expected)

