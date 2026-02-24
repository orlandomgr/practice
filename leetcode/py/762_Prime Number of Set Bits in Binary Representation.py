from myUtils.Utils import printResult
import math

class Solution:

    def countPrimeSetBits(self, left: int, right: int) -> int:
        known = {}

        def isPrime(n: int):
            number = bin(n).count("1")

            if number in known:
                return known.get(number)

            if number <= 1:
                known[number] = False
                return False
            
            # Check for factors from 2 up to the square root of the number
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    known[number] = False
                    return False # Found a factor, so it's not prime
            
            known[number] = True
            return True # No factors found, so it is prime


        result = 0
        for i in range(left, right + 1):
            # print(i)
            if isPrime(i):
                result += 1

        return result  

        
obj = Solution()

left = 6
right = 10
expected = 4
result = obj.countPrimeSetBits(left, right)
printResult(result, expected)

left = 10
right = 15
expected = 5
result = obj.countPrimeSetBits(left, right)
printResult(result, expected)
