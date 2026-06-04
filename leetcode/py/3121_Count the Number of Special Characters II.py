from typing import List
from myUtils.Utils import printResult
from collections import defaultdict
"""
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.
"""
class Solution:    

    def numberOfSpecialChars(self, word: str) -> int:
        # word = list(word)
        result = 0
        indices = defaultdict()
        wrong = {}
        for i, c in enumerate(word):
            if c in wrong:
                continue
            if c.islower() and c.upper() in indices:
                wrong[c.lower()] = 1
                wrong[c.upper()] = 1
                indices.pop(c.lower(), None)
                indices.pop(c.upper(), None)
            indices[c] = i
        keys = indices.keys()
        for k in keys:
            if k.islower():
                if k.upper() in indices:
                    if indices[k.upper()] > indices[k.lower()]:
                        result += 1 
        return result


obj = Solution()

word = "cCceDC"
expected = 0
result = obj.numberOfSpecialChars(word)
printResult(result, expected)

word = "aaAbcBC"
expected = 3
result = obj.numberOfSpecialChars(word)
printResult(result, expected)

word = "abc"
expected = 0
result = obj.numberOfSpecialChars(word)
printResult(result, expected)

word = "AbBCab"
expected = 0
result = obj.numberOfSpecialChars(word)
printResult(result, expected)
