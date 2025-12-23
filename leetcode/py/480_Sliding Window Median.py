from typing import List
from myUtils.Utils import printResult
from sortedcontainers import SortedList # type: ignore

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        res = []
        sl = SortedList()
        mid = k // 2
        for i in range(n):
            sl.add(nums[i])

            if len(sl) > k:
                sl.remove(nums[i - k])
            
            if len(sl) == k:
                if k % 2 == 0:
                    item = (sl[mid-1]+sl[mid])/2
                else:
                    item = sl[mid]
                res.append(round(item, 5))

        return res


obj = Solution()

nums = [1,3,-1,-3,5,3,6,7]
k = 3
expected = [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
result = obj.medianSlidingWindow(nums, k)
printResult(result, expected)

nums = [1,2,3,4,2,3,1,4,2]
k = 3
expected = [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]
result = obj.medianSlidingWindow(nums, k)
printResult(result, expected)