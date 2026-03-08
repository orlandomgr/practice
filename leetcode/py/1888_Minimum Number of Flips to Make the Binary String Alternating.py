from myUtils.Utils import printResult

"""
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
"""
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        # Duplicate the string to handle circular rotations
        doubled_s = s + s
        
        # Precompute mismatches for pattern starting with '0' (0,1,0,1,...)
        mismatches_pattern_01 = []
        for j in range(2 * n):
            expected = '0' if j % 2 == 0 else '1'
            mismatches_pattern_01.append(1 if doubled_s[j] != expected else 0)
        
        # Precompute mismatches for pattern starting with '1' (1,0,1,0,...)
        mismatches_pattern_10 = []
        for j in range(2 * n):
            expected = '1' if j % 2 == 0 else '0'
            mismatches_pattern_10.append(1 if doubled_s[j] != expected else 0)
        
        print(mismatches_pattern_01)
        print(mismatches_pattern_10)
        # Build prefix sums for quick range sum queries
        prefix_01 = [0] * (2 * n + 1)
        prefix_10 = [0] * (2 * n + 1)
        for j in range(1, 2 * n + 1):
            prefix_01[j] = prefix_01[j - 1] + mismatches_pattern_01[j - 1]
            prefix_10[j] = prefix_10[j - 1] + mismatches_pattern_10[j - 1]
        
        print(prefix_01)
        print(prefix_10)
        # Find the minimum flips over all possible rotations
        min_flips = float('inf')
        for i in range(n):
            # Cost for pattern 01 in this rotation
            cost_01 = prefix_01[i + n] - prefix_01[i]
            # Cost for pattern 10 in this rotation
            cost_10 = prefix_10[i + n] - prefix_10[i]
            # Take the minimum for this rotation
            min_flips = min(min_flips, cost_01, cost_10)
        
        return min_flips


obj = Solution()

s = "10001100101000000"
expected = 5
result = obj.minFlips(s)
printResult(result, expected)

s = "01001001101"
expected = 2
result = obj.minFlips(s)
printResult(result, expected)

s = "111000"
expected = 2
result = obj.minFlips(s)
printResult(result, expected)

s = "010"
expected = 0
result = obj.minFlips(s)
printResult(result, expected)

s = "1110"
expected = 1
result = obj.minFlips(s)
printResult(result, expected)

