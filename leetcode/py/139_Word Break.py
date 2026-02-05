from typing import List
from myUtils.Utils import printResult

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s [i: i + len(w)]==w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        # print(dp)
        return dp[0]

obj = Solution()

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
expected = False
result = obj.wordBreak(s, wordDict)
printResult(result, expected)

s ="catskicatcats"
wordDict = ["cats","cat","dog","ski"]
expected = True
result = obj.wordBreak(s, wordDict)
printResult(result, expected)

s = "cbca"
wordDict = ["bc","ca"]
expected = False
result = obj.wordBreak(s, wordDict)
printResult(result, expected)

s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
expected = True
result = obj.wordBreak(s, wordDict)
printResult(result, expected)

s = "cars"
wordDict = ["car","ca","rs"]
expected = True
result = obj.wordBreak(s, wordDict)
printResult(result, expected)

s = "leetcode"
wordDict = ["leet","code"]
expected = True
result = obj.wordBreak(s, wordDict)
printResult(result, expected)

s = "applepenapple"
wordDict = ["apple","pen"]
expected = True
result = obj.wordBreak(s, wordDict)
printResult(result, expected)

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
expected = False
result = obj.wordBreak(s, wordDict)
printResult(result, expected)

