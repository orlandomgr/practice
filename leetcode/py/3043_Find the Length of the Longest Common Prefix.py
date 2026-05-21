from bisect import bisect_left
from typing import List
from myUtils.Utils import printResult
"""
You are given two arrays with positive integers arr1 and arr2.

A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.

A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have common prefixes 565 and 5655 while 1223 and 43456 do not have a common prefix.

You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.

Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.

"""

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = sorted({str(x) for x in arr1})
        arr2 = sorted({str(x) for x in arr2})

        if not arr1 or not arr2:
            return 0

        def common_prefix_length(a: str, b: str) -> int:
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i

        result = 0
        for s1 in arr1:
            pos = bisect_left(arr2, s1)
            for idx in (pos - 1, pos):
                if 0 <= idx < len(arr2):
                    result = max(result, common_prefix_length(s1, arr2[idx]))
                    if result == len(s1):
                        break

        return result


obj = Solution()

arr1 = [1,10,100]
arr2 = [1000]
expected = 3
result = obj.longestCommonPrefix(arr1, arr2)
printResult(result, expected)

arr1 = [1,2,3]
arr2 = [4,4,4]
expected = 0
result = obj.longestCommonPrefix(arr1, arr2)
printResult(result, expected)

arr1 = [1,3]
arr2 = [32,22]
expected = 1
result = obj.longestCommonPrefix(arr1, arr2)
printResult(result, expected)
