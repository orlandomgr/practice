from myUtils.Utils import printResult

"""
You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise
"""
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        def swap(s1, t):
            if t == 1:
                return s1[2] + s1[1] + s1[0] + s1[3]
            else:
                return s1[0] + s1[3] + s1[2] + s1[1]

        tries = [s1]
        tries.append(swap(s1, 1))
        tries.append(swap(s1, 2))
        tries.append(swap(swap(s1, 1), 2))

        return s2 in tries
            
obj = Solution()

s1 = "abcd"
s2 = "cdab"
expected = True
result = obj.canBeEqual(s1, s2)
printResult(result, expected)

s1 = "abcd"
s2 = "dacb"
expected = False
result = obj.canBeEqual(s1, s2)
printResult(result, expected)

