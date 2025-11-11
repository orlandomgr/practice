from typing import List
from myUtils.Utils import printResult


class Solution:

    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        result = 0
        for i in range(1, n):
            if target[i - 1] > target[i]:
                result += target[i - 1] - target[i]
        result += target[-1]
        return result

    def minNumberOperations2(self, target: List[int]) -> int:
        n = len(target)
        result = [1] * n
        operations = 1

        def getRanges(arr, expected):
            i = 0
            ranges = []

            while i < n:
                # print("i: %s arr: %s exp: %s" % (i, arr[i], expected[i]))
                if arr[i] != expected[i]:
                    i += 1
                    continue
                if arr[i] == expected[i]:                
                    break
                i += 1
            if i > 0:
              ranges.append((0, i-1))

            # i = 0
            while i < n:
                # print("i: %s arr: %s exp: %s" % (i, arr[i], expected[i]))
                if arr[i] != expected[i]:
                    i += 1
                    continue

                # if not ranges and i > 0 and arr[i-1] != expected[i-1]:
                #     ranges.append((0, i - 1))
                #     continue

                j = i + 1
                while j < n:
                    # print(">>> j: %s arr: %s exp: %s" % (j, arr[j], expected[j]))
                    if arr[j] != expected[j]:
                        j += 1
                        continue

                    break
                if i + 1 < n and i + 1 <= j - 1:
                    ranges.append((i + 1, j - 1))
                i = j
            # ranges.append((i + 1, j - 1))

            return ranges

        def processRange(arr, i, j):
            while i < j:
                arr[i] += 1
                i += 1
            return arr

        ranges = getRanges(result, target)
        # print(ranges)
        # x = 0
        while True:
            while ranges:
                i, j = ranges.pop()
                result = processRange(result, i, j + 1)
                operations += 1
            ranges = getRanges(result, target)
            # print(ranges)
            # print(result)
            # x += 1
            # if x >= 8:
            #   break
            if not ranges:
                break

        # print(ranges)

        return operations


obj = Solution()

target = [7,10,3,6,3,3,3,5,5,5,9]
expected = 19
result = obj.minNumberOperations(target)
printResult(result, expected)

target = [3, 4, 2, 5, 6]
expected = 8
result = obj.minNumberOperations(target)
printResult(result, expected)

target = [1, 2, 3, 2, 1]
expected = 3
result = obj.minNumberOperations(target)
printResult(result, expected)

target = [3, 1, 1, 2]
expected = 4
result = obj.minNumberOperations(target)
printResult(result, expected)

target = [3, 1, 5, 4, 2]
expected = 7
result = obj.minNumberOperations(target)
printResult(result, expected)
