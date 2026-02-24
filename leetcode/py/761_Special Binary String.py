from myUtils.Utils import printResult

"""
Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
You are given a special binary string s.

A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them. Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.

Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.
"""

class Solution:

    def makeLargestSpecial(self, s: str) -> str:
        # Treat 1 as '(' and 0 as ')'.
        # Find all top-level balanced (special) substrings,
        # recursively optimize their insides,
        # then sort them in descending order to get the lexicographically largest result.
        count = 0
        start = 0
        subs = []

        for i, ch in enumerate(s):
            count += 1 if ch == '1' else -1
            if count == 0:
                # s[start+1 : i] is the inner part (strip outer '1' and '0')
                inner = self.makeLargestSpecial(s[start + 1 : i])
                subs.append("1" + inner + "0")
                start = i + 1

        # Sorting in descending order and concatenating gives
        # the lexicographically largest arrangement of the top-level substrings.
        subs.sort(reverse=True)
        return "".join(subs)
        
obj = Solution()

s = "101010110110100101001011110001100011100100"
expected = "111100011000111010010101001110010010101010"
result = obj.makeLargestSpecial(s)
printResult(result, expected)

s = "101101011000"
expected = "111001010010"
result = obj.makeLargestSpecial(s)
printResult(result, expected)

s = "1010101100"
expected = "1100101010"
result = obj.makeLargestSpecial(s)
printResult(result, expected)

s = "11011000"
expected = "11100100"
result = obj.makeLargestSpecial(s)
printResult(result, expected)

s = "10"
expected = "10"
result = obj.makeLargestSpecial(s)
printResult(result, expected)
