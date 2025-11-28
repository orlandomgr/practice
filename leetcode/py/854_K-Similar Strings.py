from myUtils.Utils import printResult

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)
        known = {s1}
        stack = [(s1, 0)]
        counter = 0

        while stack:
            s, counter = stack.pop(0)

            if s == s2:
                return counter
            
            for i in range(n):
                if s[i] != s2[i]:
                    break

            for j in range(i+1, n):
                if s[i] == s2[j]:
                    newS = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                    # print(newS)
                    if newS not in known:
                        stack.append((newS, counter + 1))
                        known.add(newS)
        return counter
    
obj = Solution()

s1 = "ab"
s2 = "ba"
expected = 1
result = obj.kSimilarity(s1, s2)
printResult(result, expected)

s1 = "abc"
s2 = "bca"
expected = 2
result = obj.kSimilarity(s1, s2)
printResult(result, expected)
