from typing import List
from myUtils.Utils import printResult

"""
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.
"""
class Solution:    

    def numberOfSpecialChars(self, word: str) -> int:
        word = list(set(word))
        word.sort()
        result = 0
        for c in word:
            if c.isupper():
                if c.lower() in word:
                    result += 1
            else:
                break
        return result


obj = Solution()

word = "aaAbcBC"
expected = 3
result = obj.numberOfSpecialChars(word)
printResult(result, expected)

word = "abc"
expected = 0
result = obj.numberOfSpecialChars(word)
printResult(result, expected)

word = "abBCab"
expected = 1
result = obj.numberOfSpecialChars(word)
printResult(result, expected)
