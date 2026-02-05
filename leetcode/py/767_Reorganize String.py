from typing import List
from myUtils.Utils import printResult
from collections import defaultdict, Counter, OrderedDict
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        newStr = []
        counter = Counter(s)
        pq = []
        for c, v in counter.most_common():
            heapq.heappush(pq, (-v, c))

        n = len(s)
        count = 0
        while pq:
            v, c = heapq.heappop(pq)
            prev = ""
            if len(newStr) > 0:
                prev = newStr[-1]
            tmp = []
            while pq and prev == c:
                tmp.append((v,c))
                v, c = heapq.heappop(pq)

            if prev == c:
                newStr = []
                break
            newStr.append(c)
            v += 1
            if v < 0:
                heapq.heappush(pq, (v, c))

            for v,c in tmp:
                heapq.heappush(pq, (v, c))

            count += 1
            if count > n:
                break

        # print(newStr)
        return "".join(newStr) if len(pq) == 0 else ""



obj = Solution()

s = "aabbcc"
expected = "abcabc"
result = obj.reorganizeString(s)
printResult(result, expected)

s = "abbabba"
expected = "bababab"
result = obj.reorganizeString(s)
printResult(result, expected)

s = "baaba"
expected = "ababa"
result = obj.reorganizeString(s)
printResult(result, expected)

s ="vvvlo"
expected = "vlvov"
result = obj.reorganizeString(s)
printResult(result, expected)

s = "aab"
expected = "aba"
result = obj.reorganizeString(s)
printResult(result, expected)

s = "aaab"
expected = ""
result = obj.reorganizeString(s)
printResult(result, expected)
