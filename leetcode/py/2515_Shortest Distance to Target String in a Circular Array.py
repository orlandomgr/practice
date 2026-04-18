from typing import List
from myUtils.Utils import printResult

"""
You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.
"""

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        
        idx = words.index(target)
        if idx + 1 == startIndex:
            return 1

        i = j = startIndex
        result = None
        count = 0
        while not result:
            if words[i] == target or words[j] == target:
                result = count
                break
            i += 1
            j -= 1
            if i == len(words):
                i = 0
            if j < 0:
                j = len(words) - 1
            count += 1
        return result

obj = Solution()

words = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"]
target = "zemkwvqrww"
startIndex = 8
expected = 4
result = obj.closestTarget(words, target, startIndex)
printResult(result, expected)

words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1
expected = 1
result = obj.closestTarget(words, target, startIndex)
printResult(result, expected)

words = ["a","b","leetcode"]
target = "leetcode"
startIndex = 0
expected = 1
result = obj.closestTarget(words, target, startIndex)
printResult(result, expected)

words = ["i","eat","leetcode"]
target = "ate"
startIndex = 0
expected = -1
result = obj.closestTarget(words, target, startIndex)
printResult(result, expected)
