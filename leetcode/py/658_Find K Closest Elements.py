from typing import List
from myUtils.Utils import printResult

class Solution:

    # An integer a is closer to x than an integer b if:

    # |a - x| < |b - x|, or
    # |a - x| == |b - x| and a < b

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr) - k
        while low < high:
            mid = low + (high - low) // 2
            if x <= arr[mid]:
                high = mid
            elif arr[mid + k] <= x:
                low = mid + 1
            else:
                middist = abs(x - arr[mid])
                midkdist = abs(x - arr[mid + k])
                if middist <= midkdist:
                    high = mid
                else:
                    low = mid + 1
        return arr[low : low + k]


obj = Solution()

arr = [-2, -1, 1, 2, 3, 4, 5]
k = 7
x = 3
expected = [-2, -1, 1, 2, 3, 4, 5]
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
