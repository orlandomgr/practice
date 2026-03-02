from myUtils.Utils import printResult


class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
        # nList = list(n)
        # nList.sort()
        # return int(nList[-1])
        # maxNum = -10**10
        # for i in range(len(n)):
        #     maxNum = max(maxNum, int(n[i]))

        # return maxNum


obj = Solution()

n = "32"
expected = 3
result = obj.minPartitions(n)
printResult(result, expected)

n = "82734"
expected = 8
result = obj.minPartitions(n)
printResult(result, expected)

# 10000 11100 11100 10100 10101 10111 10111 10111

n = "27346209830709182346"
expected = 9
result = obj.minPartitions(n)
printResult(result, expected)

