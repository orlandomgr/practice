from typing import List
from myUtils.Utils import printResult

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        tmp = []
        i = 0
        j = 0
        while i < m or j < n:
            if i < m:
                num1 = nums1[i]
            else:
                num1 = 10**10

            if j < n:
                num2 = nums2[j]
            else:
                num2 = 10**10

            # print("n1: %s n2: %s" %(num1, num2))
            x = min(num1, num2)
            if x == num1:
                i += 1
            elif x == num2:
                j += 1

            tmp.append(x)
        for i in range(n+m):
            nums1[i] = tmp[i]
        # print(tmp)
        # print(nums1)


obj = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
expected = [1, 2, 2, 3, 5, 6]
result = obj.merge(nums1, m, nums2, n)
printResult(nums1, expected)

nums1 = [1]
m = 1
nums2 = []
n = 0
expected = [1]
result = obj.merge(nums1, m, nums2, n)
printResult(nums1, expected)


nums1 = [0]
m = 0
nums2 = [1]
n = 1
expected = [1]
result = obj.merge(nums1, m, nums2, n)
printResult(nums1, expected)
