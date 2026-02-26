from myUtils.Utils import printResult

class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        n = int(s, 2)
        # print(n)
        while n != 1:
            result += 1
            if n&1:
                n += 1 
            else:
                n >>= 1
        return result

        
obj = Solution()

s = "1111011110000011100000110001011011110010111001010111110001"
expected = 85
result = obj.numSteps(s)
printResult(result, expected)

s = "1101"
expected = 6
result = obj.numSteps(s)
printResult(result, expected)

s = "10"
expected = 1
result = obj.numSteps(s)
printResult(result, expected)

s = "1"
expected = 0
result = obj.numSteps(s)
printResult(result, expected)
