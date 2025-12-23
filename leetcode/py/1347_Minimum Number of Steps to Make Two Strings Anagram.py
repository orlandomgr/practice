from myUtils.Utils import printResult
from typing import List
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:

        # def removeChars(string1, string2):
        #     for i in string2:
        #         string1 = string1.replace(i, '', 1)
        #     return string1

        # diff = removeChars(t, s)
        # print(diff)

        sCounter = Counter(s)
        tCounter = Counter(t)

        sKeys = sCounter.keys()
        tKeys = tCounter.keys()

        # print(sCounter)
        # print(tCounter)
        diffs = 0
        for c in sKeys:
            if c in tKeys:
                diffs += abs(sCounter[c]-tCounter[c])
                del tCounter[c]
            else:
                diffs += sCounter[c]

        for c in tKeys:
            diffs += tCounter[c]


        return diffs // 2


obj = Solution()

s = "bab"
t = "aba"
expected = 1
result = obj.minSteps(s, t)
printResult(result, expected)

s = "leetcode"
t = "practice"
expected = 5
result = obj.minSteps(s, t)
printResult(result, expected)

s = "anagram"
t = "mangaar"
expected = 0
result = obj.minSteps(s, t)
printResult(result, expected)
