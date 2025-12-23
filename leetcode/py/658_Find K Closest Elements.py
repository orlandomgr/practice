from typing import List
from myUtils.Utils import printResult

class Solution:

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = x
        right = x
        if left < 0:
            left = 0

        if right >= len(arr):
            right = len(arr) - 1

        def isCloser(a:int, b:int, x: int):
            # print("isCloser a: %s b: %s x: %s" %(a,b,x))
            # return a - x < b - x or a - x == b - x and x < b
            if not a:
                return False
            if not b:
                return True
            return a < b or a == b and x < b

        res = []
        n = len(res)
        # print("left: %s" %(left))       
        while n < k:
            if 0 <= left < len(arr):
                a = arr[left]
            else:
                a = None

            if 0 <= right < len(arr):
                b = arr[right]
            else:
                b = None

            # if a == None:
            #     a = b

            # if b == None:
            #     b = a

            if isCloser(a, b, x):
                res.append(a)
            else:
                res.append(b)

            left -= 1
            right += 1

            #     if 0 <= left < len(arr) - 1:
            #         b = arr[left+1]
            #         if isCloser(a, b, x):
            #             res.append(arr[left])
            #         else:
            #             res.append(arr[left+1])
            #     elif 0 <= left < len(arr) :
            #         b = arr[left-1]
            #         if isCloser(a, b, x):
            #             res.append(arr[left])
            #         else:
            #             res.append(arr[left-1])

            #     else:
            #         res.append(arr[left])
            # if toLeft:
            #     left -= 1
            # else:
            #     left += 1
            n = len(res)

        print(res)
        res.sort()
        return res

obj = Solution()

arr = [-2,-1,1,2,3,4,5]
k = 7
x = 3
expected = [-2,-1,1,2,3,4,5]
result = obj.findClosestElements(arr, k, x)
printResult(result, expected)

# arr = [1,2]
# k = 1
# x = 1
# expected = [1]
# result = obj.findClosestElements(arr, k, x)
# printResult(result, expected)

# arr = [1]
# k = 1
# x = 1
# expected = [1]
# result = obj.findClosestElements(arr, k, x)
# printResult(result, expected)

# arr = [1,2,3,4,5]
# k = 4
# x = 3
# expected = [1,2,3,4]
# result = obj.findClosestElements(arr, k, x)
# printResult(result, expected)

# arr = [1,1,2,3,4,5]
# k = 4
# x = -1
# expected = [1,1,2,3]
# result = obj.findClosestElements(arr, k, x)
# printResult(result, expected)

