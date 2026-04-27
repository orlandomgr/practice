from typing import List
from myUtils.Utils import printResult
from collections import Counter

"""
You are given two string arrays, queries and dictionary. All words in each array comprise of lowercase English letters and have the same length.

In one edit you can take a word from queries, and change any letter in it to any other letter. Find all words from queries that, after a maximum of two edits, equal some word from dictionary.

Return a list of all words from queries, that match with some word from dictionary after a maximum of two edits. Return the words in the same order they appear in queries.
"""

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def isBelow2Diffs(s1, s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
                if count > 2:
                    return False
            return True
        
        result = []
        for q in queries:
            for d in dictionary:
                if isBelow2Diffs(q, d):
                    result.append(q)
                    break
        return result

obj = Solution()

queries = ["t","i","m","i","p","s"]
dictionary = ["w","j","b","p","u","b","u","i","h","m"]
expected = ["t","i","m","i","p","s"]
result = obj.twoEditWords(queries, dictionary)
printResult(result, expected)

queries = ["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"]
dictionary = ["uyj","bug","dba","xbe","blu","wuo","tsf","tga"]
expected = ["word","note","wood"]
result = obj.twoEditWords(queries, dictionary)
printResult(result, expected)

queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]
expected = ["word","note","wood"]
result = obj.twoEditWords(queries, dictionary)
printResult(result, expected)

queries = ["yes"]
dictionary = ["not"]
expected = []
result = obj.twoEditWords(queries, dictionary)
printResult(result, expected)
