from typing import List
from myUtils.Utils import printResult

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for w in words:
            for candidate in w.split(separator):
                if candidate:
                    result.append(candidate)
            # if separator in w:
            #     while w:
            #         idx = w.find(separator)
            #         if idx == -1:
            #             result.append(w)
            #             break
            #         newW = w[:idx]
            #         w = w[idx+1:]
            #         # print(w)
            #         if newW:
            #             result.append(newW)
            #         # break
            # else:
            #     result.append(w)
        return result
            
obj = Solution()

words = ["one.two.three","four.five","six"]
separator = "."
expected = ["one","two","three","four","five","six"]
result = obj.splitWordsBySeparator(words, separator)
printResult(result, expected)

words = ["$easy$","$problem$"]
separator = "$"
expected = ["easy","problem"]
result = obj.splitWordsBySeparator(words, separator)
printResult(result, expected)

words = ["|||"]
separator = "|"
expected = []
result = obj.splitWordsBySeparator(words, separator)
printResult(result, expected)
