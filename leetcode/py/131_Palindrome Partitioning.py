from typing import List
from myUtils.Utils import printResult

class Solution:

    def isPalindrome(self, s: str, i, j):
        left = i
        right = j
        while left < right:  
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        part = []

        def dfs(i):
            if i >= n:
                res.append(part.copy())
                return
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return res
    
obj = Solution()

s = "fff"
expected = [["f","f","f"],["f","ff"],["ff","f"],["fff"]]
result = obj.partition(s)
printResult(result, expected)

s = "efe"
expected = [["e","f","e"],["efe"]]
result = obj.partition(s)
printResult(result, expected)

s = "ab"
expected = [["a","b"]]
result = obj.partition(s)
printResult(result, expected)

s = "aab"
expected = [["a","a","b"],["aa","b"]]
result = obj.partition(s)
printResult(result, expected)

s = "a"
expected = [["a"]]
result = obj.partition(s)
printResult(result, expected)

