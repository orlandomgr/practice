from myUtils.Utils import printResult
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        maxCount = 0
        count = 0
        known = defaultdict(int)
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            if c in known:
                maxCount = max(maxCount, count)
                count = 0
                i = known[c] + 1
                known.clear()
            else:
                count += 1
                known[c] = i
                i += 1
        maxCount = max(maxCount, count)

        return maxCount
    
obj = Solution()

s = "dvdf"
expected = 3
result = obj.lengthOfLongestSubstring(s)
printResult(result, expected)

s = "aab"
expected = 2
result = obj.lengthOfLongestSubstring(s)
printResult(result, expected)

s = "abcabcbb"
expected = 3
result = obj.lengthOfLongestSubstring(s)
printResult(result, expected)

s = "bbbbb"
expected = 1
result = obj.lengthOfLongestSubstring(s)
printResult(result, expected)

s = "pwwkew"
expected = 3
result = obj.lengthOfLongestSubstring(s)
printResult(result, expected)
