from typing import List
from myUtils.Utils import printResult

class Solution:
    def divideOrMultiply(self, stack: List, i: int, isMultiplication: bool = True):
        n2 = stack[i+1]
        n1 = stack[i-1]
        if isMultiplication:
            stack[i] = n1 * n2
        else:
            stack[i] = n1 // n2
        stack.pop(i-1)
        stack.pop(i)
        return stack

    def compute(self, s: str) -> int:
        i = 0
        n = len(s)
        stack = []
        while i < n:
            if s[i] == "/" or s[i] == "*" or s[i] == "+":
                stack.append(s[i])
                i += 1
            elif s[i] == "-":
                if stack and stack[-1] == "-":
                    stack[-1] = "+"
                elif stack and stack[-1] == "+":
                    stack[-1] = "-"
                else:
                    stack.append("-")
                i += 1
            elif s[i].isdigit():
                num = int(s[i])
                i += 1
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(num)
            else:
                i += 1

        # print(stack)
        hasMorD = True
        while hasMorD:
            iM = 10**10
            iD = 10**10
            if "*" in stack:
                try:
                    iM = stack.index("*")    
                except:
                    iM = 10**10
            if "/" in stack:
                try:
                    iD = stack.index("/")
                except:
                    iD = 10**10

            # print("m: %s d: %s" %(iM, iD))
            if iM < iD and 0 <= iM < len(stack):
                # print("mult")
                self.divideOrMultiply(stack, iM, True)
            elif iD < iM and 0 <= iD < len(stack):
                # print("div")
                self.divideOrMultiply(stack, iD, False)
            
            if "*" not in stack and "/" not in stack:
                hasMorD = False

        # print(stack)
 
        result = stack[0]
        start = 1
        if result == "-":
            result = -stack[1]
            start = 2
        if result == "+":
            result = stack[1]
            start = 2

        for i in range(start, len(stack), 2):
            if stack[i] == "+":
                result += stack[i+1]
            elif stack[i] == "-":
                result -= stack[i+1]
        # print ("result: %s" %(result)) 
        return result # eval(s)

    def calculate(self, s: str) -> int:
        s = "".join(s.split())
        return self.compute(s)
   
obj = Solution()

s = "14/3/2"
expected = 2
result = obj.calculate(s)
printResult(result, expected)

s = "0"
expected = 0
result = obj.calculate(s)
printResult(result, expected)

s = "14/3*2"
expected = 8
result = obj.calculate(s)
printResult(result, expected)

s = "-3*3+3"
expected = -6
result = obj.calculate(s)
printResult(result, expected)

s = "-3*3+12"
expected = 3
result = obj.calculate(s)
printResult(result, expected)


s = "3+2*2"
expected = 7
result = obj.calculate(s)
printResult(result, expected)

s = " 3/2 "
expected = 1
result = obj.calculate(s)
printResult(result, expected)

s = " 3+5 / 2 "
expected = 5
result = obj.calculate(s)
printResult(result, expected)

