from myUtils.Utils import printResult

"""
Given two positive integers n and k, the binary string Sn is formed as follows:

S1 = "0"
Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, 
and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.
"""
class Solution:

    def invert(self, s: str):
        s = s.replace("0", "2")
        s = s.replace("1", "0")
        s = s.replace("2", "1")
        return s 
    
    def reverse(self, s: str):
        return s[::-1]
    
    def getSN(self, n):
        if n == 1:
            return "0"
        
        num = self.getSN(n - 1)
        return num + "1" + self.reverse(self.invert(num))
    
    def findKthBit(self, n: int, k: int) -> str:
        s = self.getSN(n)
        return s[k-1]

obj = Solution()

n = 3
k = 1
expected = "0"
result = obj.findKthBit(n, k)
printResult(result, expected)

n = 4
k = 11
expected = "1"
result = obj.findKthBit(n, k)
printResult(result, expected)
