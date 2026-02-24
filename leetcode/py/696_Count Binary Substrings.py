from myUtils.Utils import printResult

class Solution:
    def getNext(self, s: str) -> str:
        if s == "1":
            return "0"
        else:
            return "1"

    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        result = []
        i = 0
        while i < n:
            currS = s[i]
            nextS = self.getNext(currS)

            next = s.find(nextS, i + 1)
            if next == -1:
                break

            limit = s.find(currS, next + 1)
            if limit == -1:
                limit = n
            
            left = next - i
            right = limit - next

            if left == right:
                size = left
            else:
                size = min(right, left)

            # print(f"left: {left} right: {right} size: {size}")
            if size > 0:
                for x in range(size):
                    result.append(x)
                i = next
            else:
                i += 1
        return len(result)
        
obj = Solution()

s = "10"
expected = 1
result = obj.countBinarySubstrings(s)
printResult(result, expected)

s = "1100"
expected = 2
result = obj.countBinarySubstrings(s)
printResult(result, expected)

s = "1010"
expected = 3
result = obj.countBinarySubstrings(s)
printResult(result, expected)

s = "111000"
expected = 3
result = obj.countBinarySubstrings(s)
printResult(result, expected)

s = "11110000"
expected = 4
result = obj.countBinarySubstrings(s)
printResult(result, expected)

s = "1111000011"
expected = 6
result = obj.countBinarySubstrings(s)
printResult(result, expected)
