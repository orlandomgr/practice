from myUtils.Utils import printResult

class Solution:
    def decodeString(self, s: str) -> str:
        hasInner = "[" in s
        while hasInner:
            lIdx = s.rfind("[")
            rIdx = s.find("]", lIdx)
            i = lIdx-1
            num = ""
            while True:
                if i < 0:
                    break
                c = s[i] 
                if c.isdigit():
                    num = c + num 
                    i -= 1
                else:
                    break
            
            newS = s[lIdx+1:rIdx] * int(num)
            s = s[:i+1] + newS + s[rIdx+1:]
            hasInner = "[" in s
        return s
    

obj = Solution()

s = "3[a]2[bc]"
expected = "aaabcbc"
result = obj.decodeString(s)
printResult(result, expected)

s = "3[a2[c]]"
expected =  "accaccacc"
result = obj.decodeString(s)
printResult(result, expected)

s = "2[abc]3[cd]ef"
expected =  "abcabccdcdcdef"
result = obj.decodeString(s)
printResult(result, expected)
