from typing import List
from myUtils.Utils import printResult
from functools import cache
from collections import Counter
import queue
import math

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
      n = len(words)

      def isAnagram(word1:str, word2:str):
         if len(word1) != len(word2):
            return False
         if sorted(word1) == sorted(word2):
            return True
         return False

      i = 0
      while i < n - 1:
         w1 = words[i]
         w2 = words[i + 1]
         if isAnagram(w1, w2):
            words.remove(w2)
            n = len(words)
            continue
         i += 1
         
      return words    


obj = Solution()

words = ["abba","baba","bbaa","cd","cd"]
expected = ["abba","cd"]
result = obj.removeAnagrams(words)
printResult(result, expected)

words = ["a","b","c","d","e"]
expected = ["a","b","c","d","e"]
result = obj.removeAnagrams(words)
printResult(result, expected)



