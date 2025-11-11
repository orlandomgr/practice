from typing import List
from myUtils.Utils import printResult


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        result = 0
        ages.sort(reverse=True)

        count = [0] * 500
        for age in ages:
            count[age] += 1

        # print (count)
        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB: continue
                if ageA < ageB: continue
                if ageA < 100 < ageB: continue
                ans += countA * countB
                if ageA == ageB: ans -= countA

        return ans

        # n = len(ages)
        # friendPointer = 0
        # for xIdx in range(n):
        #     x = ages[xIdx]
        #     while friendPointer < n and \
        #     x // 2 + 7 <= ages[friendPointer]:
        #       friendPointer += 1
        #     result += friendPointer - xIdx - 1


        for xIdx, x in enumerate(ages):
          for yIdx, y in enumerate(ages):
            # for yIdx in range(xIdx + 1, n):
                if xIdx == yIdx:
                    continue
                y = ages[yIdx]
                #  print("x: %s %s y: %s" %(x, .5 * x + 7, y))
                if (y > x) or (y > 100 and x < 100) or (y <= 0.5 * x + 7):
                    continue
                print("%s -> %s" %(x,y))
                result += 1

        return result


obj = Solution()

ages = [16, 16]
expected = 2
result = obj.numFriendRequests(ages)
printResult(result, expected)

ages = [16, 17, 18]
expected = 2
result = obj.numFriendRequests(ages)
printResult(result, expected)

ages = [20, 30, 100, 110, 120]
expected = 3
result = obj.numFriendRequests(ages)
printResult(result, expected)

ages = [45, 55, 88, 101, 120, 230, 300, 400]
expected = 8
result = obj.numFriendRequests(ages)
printResult(result, expected)

ages = [45, 55, 88, 101, 120]
expected = 5
result = obj.numFriendRequests(ages)
printResult(result, expected)
