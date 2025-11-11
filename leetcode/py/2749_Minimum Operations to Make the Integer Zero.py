# You are given two integers num1 and num2.
# In one operation, you can choose integer i in the range [0, 60] and subtract 2i + num2 from num1.
# Return the integer denoting the minimum number of operations needed to make num1 equal to 0.
# If it is impossible to make num1 equal to 0, return -1.

# Example 1:

# Input: num1 = 3, num2 = -2
# Output: 3
# Explanation: We can make 3 equal to 0 with the following operations:
# - We choose i = 2 and subtract 2^2 + (-2) from 3, 3 - (4 + (-2)) = 1.
# - We choose i = 2 and subtract 2^2 + (-2) from 1, 1 - (4 + (-2)) = -1.
# - We choose i = 0 and subtract 2^0 + (-2) from -1, (-1) - (1 + (-2)) = 0.
# It can be proven, that 3 is the minimum number of operations that we need to perform.
# Example 2:

# Input: num1 = 5, num2 = 7
# Output: -1
# Explanation: It can be proven, that it is impossible to make 5 equal to 0 with the given operation.

class Solution:
    def calculate (self, power, n1, n2):
        # print("n1: %s n2: %s power: %s" %(n1, n2, power))
        return n1 - (power + n2)
    
    def getNearValue(self, power, n1: int, n2: int) -> int:
        array = list(map(lambda item: self.calculate(item, n1, n2), power))
        # print(array)
        closest_num = array[0]
        for num in array:
            # Compare absolute values
            if abs(num) < abs(closest_num):
                closest_num = num
                # idx = index
            # If absolute values are equal, choose the positive one
            # elif abs(num) == abs(closest_num) and num > closest_num:
            #     closest_num = num
            #     idx = index
        return closest_num

    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # n = num1 - num2
        # n = num1
        # power = [0] * 61
        # for i in range(61):
        #     power[i] = 2 ** i

        # times = 1
        # while times < 61:
        #     value = self.getNearValue(power, n, num2)
        #     print("n1: %s value: %s" %(n, value))
        #     if(value == 0):
        #         break
        #     n = value
        #     # print("n: %s value: %s" %(n, value))
        #     times += 1
        # # print(n.bit_count())

        # # print(times)
        # if(times == 61):
        #     times = -1
        # return times 
    
        counter = 1
        while True:
            calc = num1 - num2 * counter
            if calc < counter:
                return -1
            if counter >= calc.bit_count():
                return counter
            counter += 1       
                    
obj = Solution()
print(obj.makeTheIntegerZero(3, -2)) # 3
print(obj.makeTheIntegerZero(5, 7)) # -1
print(obj.makeTheIntegerZero(5, -21)) # 3
