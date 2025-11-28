from myUtils.Utils import printResult

class Solution:

    def compute(self, s: str) -> int:
        i = 0
        n = len(s)
        stack = []
        while i < n:
            if s[i] == "+":
                # if stack and type(stack[-1]) is int:
                stack.append("+")
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
            else:
                result -= stack[i+1]
        # print ("result: %s" %(result)) 
        return result # eval(s)

    def calculate(self, s: str) -> int:
        s = "".join(s.split())
        left = s.rfind("(")
        right = s.find(")", left)
        while left >= 0:
            val = self.compute(s[left+1:right])
            s = str(s[:left]) + str(val) + str(s[right+1:])
            left = s.rfind("(")
            right = s.find(")", left)

        return self.compute(s)
   
obj = Solution()

s = "-(-2)+4"
expected = 6
result = obj.calculate(s)
printResult(result, expected)

s = "- (3 + (4 + 5))"
expected = -12
result = obj.calculate(s)
printResult(result, expected)

s="1-(     -2)"
expected = 3
result = obj.calculate(s)
printResult(result, expected)

s = "-5 + 1 + 1"
expected = -3
result = obj.calculate(s)
printResult(result, expected)

s = "1 + 1"
expected = 2
result = obj.calculate(s)
printResult(result, expected)

s = " 2-1 + 2 "
expected = 3
result = obj.calculate(s)
printResult(result, expected)

s = "(1+(4+5+2)-3)+(6+8)"
expected = 23
result = obj.calculate(s)
printResult(result, expected)
