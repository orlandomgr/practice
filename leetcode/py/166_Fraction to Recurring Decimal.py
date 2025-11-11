import math


class Solution:

    # def getEnclosingResult(self, result: str) -> str:
    #     dotIdx = result.find(".")
    #     if dotIdx == -1:
    #         return result
    #     if result.endswith(".0"):
    #         return result[0:dotIdx]

    #     enclosed = result[0:2]
    #     result = result[2:]
    #     size = len(result)
    #     if size < 8:
    #         return (enclosed + result)
    #     found = False
    #     for i in range(17):
    #         if found:
    #             break
    #         for j in range(1, 17):
    #             sub = result[i:i+j]
    #             regex = sub * (math.ceil(16 // j))
    #             print("sub: %s multiplier: %s regex: %s" %(sub, (math.ceil(16 // j)), regex))
    #             if result.find(regex, i+j) != -1:
    #                 found = True
    #                 print(sub)
    #                 break
    #         if not found:
    #             enclosed += result[i:i+1]
    #     print(found)
    #     enclosed += "(" + sub + ")"
    #     return enclosed

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)

        result = sign
        result += str(int(numerator // denominator))

        remainder = numerator % denominator

        if remainder == 0:
            return result

        result += "."
        remainders = {}

        numerator %= denominator
        idx = 0
        part = ""
        remainders = {numerator: idx}
        while numerator % denominator:
            numerator *= 10
            idx += 1
            remainder = numerator % denominator
            part += str(numerator // denominator)
            if remainder in remainders:
                part = (
                    part[: remainders[remainder]]
                    + "("
                    + part[remainders[remainder] :]
                    + ")"
                )
                return result + part

            remainders[remainder] = idx
            numerator = remainder
        return result + part
        # remainders[remainder] = len(result)
        # remainder *= 10
        # result += str(numerator/ denominator)[1:]
        # remainder %= denominator
        # result += str(10 * remainder / denominator)
        # remainder = 10 * remainder % denominator

        # print(remainder)
        # idx = remainders[remainder]
        # result = result[:idx] + "(" + result[idx+1:] + ")"
        # return result

def printResult(result, expected):
    if result == expected:
        print("\033[92mpassed: %s result: %s expected: %s\033[0m" % (result == expected, result, expected))
    else:
        print("\033[91mpassed: %s result: %s expected: %s\033[0m" % (result == expected, result, expected))


obj = Solution()

numerator = 1
denominator = 2
expected = "0.5"
result = obj.fractionToDecimal(numerator, denominator)
printResult(result, expected)

numerator = 2
denominator = 1
expected = "2"
result = obj.fractionToDecimal(numerator, denominator)
printResult(result, expected)

numerator = 4
denominator = 333
expected = "0.(012)"
result = obj.fractionToDecimal(numerator, denominator)
printResult(result, expected)

numerator = 1
denominator = 99
expected = "0.(01)"
result = obj.fractionToDecimal(numerator, denominator)
printResult(result, expected)

numerator = 2
denominator = 3
expected = "0.(6)"
result = obj.fractionToDecimal(numerator, denominator)
printResult(result, expected)

numerator = 1
denominator = 6
expected = "0.1(6)"
result = obj.fractionToDecimal(numerator, denominator)
printResult(result, expected)

numerator = 1
denominator = 17
expected = "0.(0588235294117647)"
result = obj.fractionToDecimal(numerator, denominator)
printResult(result, expected)
