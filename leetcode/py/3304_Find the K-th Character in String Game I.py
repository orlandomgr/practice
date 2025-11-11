class Solution:
    # 97 - 122

    def getNextChars(self, s: str) -> str:
        newS = ""
        for c in s:
            nextC = ord(c) + 1
            if nextC > 122:
                nextC = 97
            newS += chr(nextC)
        return newS
    
    def kthCharacter(self, k: int) -> str:
        if k < 0:
            return ""
        s = "a"
        while len(s) < k:
            s = self.getNextChars(s)
        return s[k-1]


obj = Solution()
print(obj.kthCharacter(1))  # a
print(obj.kthCharacter(2))  # b
print(obj.kthCharacter(3))  # b
print(obj.kthCharacter(4))  # c
print(obj.kthCharacter(5))  # b
# print(obj.kthCharacter(6))  # b
# print(obj.kthCharacter(7))  # a
# print(obj.kthCharacter(8))  # a
# print(obj.kthCharacter(9))  # b
# print(obj.kthCharacter(10))  # c

# abbcbccd
# abbcbccd

# abbcbccdbccdcdde
# bccdcdde