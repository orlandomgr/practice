from myUtils.Utils import printResult

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        arr = [0] * len(text1)

        longest = 0
        for c in text2:
            curr = 0
            for i, val in enumerate(arr):
                if curr < val:
                    curr = val
                elif c == text1[i]:
                    arr[i] = curr + 1
                    longest = max(longest, curr + 1)

        # print(arr)
        return longest
    

obj = Solution()

text1 = "pmjghexybyrgzczy"
text2 = "hafcdqbgncrcbihkd"
expected = 4
result = obj.longestCommonSubsequence(text1, text2)
printResult(result, expected)

text1 = "abcba"
text2 = "abcbcba"
expected = 5
result = obj.longestCommonSubsequence(text1, text2)
printResult(result, expected)

text1 = "bsbininm"
text2 = "jmjkbkjkv"
expected = 1
result = obj.longestCommonSubsequence(text1, text2)
printResult(result, expected)

text1 = "hofubmnylkra"
text2 = "pqhgxgdofcvmr"
expected = 5
result = obj.longestCommonSubsequence(text1, text2)
printResult(result, expected)

text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"
expected = 2
result = obj.longestCommonSubsequence(text1, text2)
printResult(result, expected)

text1 = "ezupkr"
text2 = "ubmrapg"
expected = 2
result = obj.longestCommonSubsequence(text1, text2)
printResult(result, expected)

text1 = "abcde"
text2 = "ace"
expected = 3
result = obj.longestCommonSubsequence(text1, text2)
printResult(result, expected)

text1 = "abc"
text2 = "abc"
expected = 3
result = obj.longestCommonSubsequence(text1, text2)
printResult(result, expected)

text1 = "abc"
text2 = "def"
expected = 0
result = obj.longestCommonSubsequence(text1, text2)
printResult(result, expected)
