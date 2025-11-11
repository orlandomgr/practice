class Solution:
    def encode(self, s):
        result = ""
        tmp = ""
        counter = 0
        for c in s:
            if tmp == "":
                tmp = c
            if tmp != c:
                result += str(counter) + tmp
                # print("counter: %s c: %s result: %s" %(counter, c, result))
                counter = 0
                tmp = c
            counter += 1
            tmp = c
        result += str(counter) + tmp
        # print("str: %s result: %s" %(s, result))
        return result

    def countAndSay(self, n: int) -> str:
        # print("n: %s" %(n) )
        if n < 1:
            return
        if n == 1:
            return "1"
        if n == 2:
            return "11"
        return self.encode(self.countAndSay(n - 1))

obj = Solution()
# print(obj.countAndSay(1))
print(obj.countAndSay(4))
print(obj.countAndSay(5))


# Example 1:

# Input: n = 4

# Output: "1211"

# Explanation:

# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# Example 2:

# Input: n = 1

# Output: "1"

# Explanation:

# This is the base case.