from myUtils.Utils import printResult

class Solution:
    # 97 a
    # 122 z
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        charCount = [0] * 26

        for c in s:
            val = ord(c) - 97
            charCount[val] += 1

        for x in range(t):
            temp1 = charCount[0]
            charCount[0] = 0
            for i in range(1, 26):
                temp2 = charCount[i]
                charCount[i] = temp1
                temp1 = temp2
                if i == 25:
                    charCount[0] += temp1 # a
                    charCount[1] += temp1 # b

        result = sum(charCount) % ((10 ** 9) + 7)
        return result

# print(79033769 * ((10 ** 9) + 7))
# print(((2 ** 313)))
obj = Solution()
# 2
# 3
# 5
# 1,2,4,8,16,32
# tuuvuvvwuvvwvwwx
s = "a"
t = 123
expected = 16
result = obj.lengthAfterTransformations(s, t)
printResult(result, expected)

# 79033769553236383
# 79033769

s = "jqktcurgdvlibczdsvnsg"
t = 7517
expected = 79033769
result = obj.lengthAfterTransformations(s, t)
printResult(result, expected)

s = "abcyy"
t = 2
expected = 7
result = obj.lengthAfterTransformations(s, t)
printResult(result, expected)

s = "azbk"
t = 1
expected = 5
result = obj.lengthAfterTransformations(s, t)
printResult(result, expected)

s = ""
t = 1
expected = 0
result = obj.lengthAfterTransformations(s, t)
printResult(result, expected)

s = "cu"
t = 5
expected = 2
result = obj.lengthAfterTransformations(s, t)
printResult(result, expected)

s = "azbk"
t = 1
expected = 5
result = obj.lengthAfterTransformations(s, t)
printResult(result, expected)
