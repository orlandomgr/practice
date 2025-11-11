from typing import List

# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word.

class Solution:
    def printVertically(self, s: str) -> List[str]:
        r = []
        result = ""
        arr = s.split(" ")

        # idx = 0
        maxIdx = 0

        for a in arr:
            maxIdx = max(maxIdx, len(a))

        for i in range(maxIdx):
            for a in arr:
                if i < len(a):
                    result += a[i]
                else:
                    result += " "
            r.append(result.rstrip())
            result = ""
        return r


obj = Solution()
print(obj.printVertically("HOW ARE YOU"))
print(obj.printVertically("TO BE OR NOT TO BE"))
print(obj.printVertically("CONTEST IS COMING"))

# Example 1:

# Input: s = "HOW ARE YOU"
# Output: ["HAY","ORO","WEU"]
# Explanation: Each word is printed vertically. 
#  "HAY"
#  "ORO"
#  "WEU"
# Example 2:

# Input: s = "TO BE OR NOT TO BE"
# Output: ["TBONTB","OEROOE","   T"]
# Explanation: Trailing spaces is not allowed. 
# "TBONTB"
# "OEROOE"
# "   T"
# Example 3:

# Input: s = "CONTEST IS COMING"
# Output: ["CIC","OSO","N M","T I","E N","S G","T"]