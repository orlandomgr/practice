from typing import List
from myUtils.Utils import printResult
from functools import cache

"""
Find the minimum total distance to type a word using two fingers on a 6-column keyboard.
The Manhattan distance between letters is used, and initial finger placements are free.
"""

class Solution:
    def minimumDistance(self, word: str) -> int:
        # Distance between keys a and b on a 6-column grid. Returns 0 for free starting move.
        def d(a, b):
            if a < 0: return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)

        A = [ord(c) - 65 for c in word]

        @cache
        def solve(i, f2):
            if i == len(A): return 0
            # f1 is the finger that typed the previous character
            f1 = A[i - 1] if i > 0 else -1
            
            # Choice: Move f1 to A[i] or move f2 to A[i]
            return min(d(f1, A[i]) + solve(i + 1, f2), 
                       d(f2, A[i]) + solve(i + 1, f1))

        return solve(0, -1)

obj = Solution()

word = "CAKE"
expected = 3
result = obj.minimumDistance(word)
printResult(result, expected)

word = "HAPPY"
expected = 6
result = obj.minimumDistance(word)
printResult(result, expected)

word = "NEW"
expected = 3
result = obj.minimumDistance(word)
printResult(result, expected)

word = "YEAR"
expected = 7
result = obj.minimumDistance(word)
printResult(result, expected)
