from typing import List
from myUtils.Utils import printResult
from functools import cache
from itertools import permutations
import heapq


class Solution:
    def countSubstringsHelper(self, s: str, size: int, i: int, evenIdx: int, oddIdx: int) -> int:
        isEven = True
        isOdd = True
        count = 1

        while i >= 0 and (isEven or isOdd): 
            if isEven and evenIdx < size and s[i] == s[evenIdx]:
                count += 1
                evenIdx += 1
            else:
                isEven = False

            if isOdd and oddIdx < size and s[i] == s[oddIdx]:
                count += 1
                oddIdx += 1
            else:
                isOdd = False

            i -= 1
        return count

    def countSubstrings(self, s: str) -> int:
        size = len(s)
        count = 0
        i = 0
        for i in range(size):
            count += self.countSubstringsHelper(s, size, i, i + 1, i + 2)
        return count

    def countSubstringsBF(self, s: str) -> int:
        size = len(s)
        count = 0
        for i in range(1, size + 1):
            for j in range(size - i + 1):
                p = s[j : j + i]
                if p and p == p[::-1]:
                    print(p)
                    count += 1
        return count


obj = Solution()

nums = "holohffh"
expected = 12
result = obj.countSubstrings(nums)
printResult(result, expected)

nums = "fdsklf"
expected = 6
result = obj.countSubstrings(nums)
printResult(result, expected)

nums = "aaaaa"
expected = 15
result = obj.countSubstrings(nums)
printResult(result, expected)

nums = "aaa"
expected = 6
result = obj.countSubstrings(nums)
printResult(result, expected)

nums = "ab"
expected = 2
result = obj.countSubstrings(nums)
printResult(result, expected)

nums = "abc"
expected = 3
result = obj.countSubstrings(nums)
printResult(result, expected)

nums = "dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"
expected = 77
result = obj.countSubstrings(nums)
printResult(result, expected)

nums = "kmbwncsafwowithnzvzgyvvgshbs"
expected = 31
result = obj.countSubstrings(nums)
printResult(result, expected)

nums = "bbccaacacdbdbcbcbbbcbadcbdddbabaddbcadb"
expected = 64
result = obj.countSubstrings(nums)
printResult(result, expected)

nums = (
    "addaccadbabdbdbdbcabdcbcadacccbdddcbddacdaacbbdcbdbccdaaddadcaacdacbaaddbcaadcdab"
)
expected = 126
result = obj.countSubstrings(nums)
printResult(result, expected)
