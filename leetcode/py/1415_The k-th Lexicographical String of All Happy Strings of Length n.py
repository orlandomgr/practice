from typing import List
from myUtils.Utils import printResult
import math
import heapq
import itertools

"""
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.
"""
class Solution:

    def appendCombinations(self, current, options):
        result = []
        for o in options:
            if current[-1] == o:
                continue
            else:                    
                result.append((current + o))
        return result 
    
    def getCombinations(self, options, size):
        result = []
        if size <= 0:
            return result 
        
        for o in options:
            result.append(o)

        while len(result[0]) < size:
            tmp = []
            while len(result) > 0:
                current = result.pop()
                tmp += self.appendCombinations(current, options)

            result = tmp

        return result


    def getHappyString(self, n: int, k: int) -> str:
        combo = self.getCombinations(["a","b","c"], n)
        combo.sort()
        # print(combo)

        if len(combo) < k:
            return ""
        else:
            return combo[k-1]

    
obj = Solution()

# n = 1
# k = 3
# expected = "c"
# result = obj.getHappyString(n, k)
# printResult(result, expected)

# n = 1
# k = 4
# expected = ""
# result = obj.getHappyString(n, k)
# printResult(result, expected)

n = 3
k = 9
expected=  "cab"
result = obj.getHappyString(n, k)
printResult(result, expected)
