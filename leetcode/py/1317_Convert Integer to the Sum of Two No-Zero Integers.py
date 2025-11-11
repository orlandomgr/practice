from typing import List
# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        knownZeros = set()
        for i in range(1, n):
            if i in knownZeros:
                continue
            if self.containsZero(i):
                knownZeros.add(i)
                continue
            for j in range(n, 0, -1):
                if j in knownZeros:
                    continue
                if self.containsZero(j):
                    knownZeros.add(j)
                    continue
                # print("i: %s j: %s" %(i,j))
                if (i + j) == n:
                    return [i,j]

    def containsZero(self, n: int) -> bool:
        while n > 0:
            if n % 10 == 0:
                return True
            n = n // 10
        return False
        
        
obj = Solution()
print(obj.getNoZeroIntegers(2))
print(obj.getNoZeroIntegers(11))
# Example 1:

# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.
# Example 2:

# Input: n = 11
# Output: [2,9]
# Explanation: Let a = 2 and b = 9.
# Both a and b are no-zero integers, and a + b = 11 = n.
# Note that there are other valid answers as [8, 3] that can be accepted.
 