from typing import List
from myUtils.Utils import printResult
from collections import Counter
from functools import cache

class Solution:
    def xSum(self, nums: List[int], x: int) -> int:
        c = Counter(nums)
        sorted_items = sorted(c.items(), key=lambda item: (-item[1], -item[0]))
        # print(c)
        # print(sorted_items)
        result = 0
        counter = 0
        for n, times in sorted_items:
            if counter == x:
                break
            result += (n * times)
            counter += 1
        return result


    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        n = len(nums)
        known = {}
        for i in range(n - k + 1):
            # print(i)
            arr = nums[i:i+k]
            key = "-".join(str(x) for x in arr)
            if key in known:
              print("found")
              result.append(known[key])
              continue    

            res = self.xSum(arr, x)
            # print(nums[i:i+k])
            result.append(res)
            known[key] = res
        return result
    
obj = Solution()

# nums = [1,1,2,2,3,4,2,3]
# k = 6
# x = 2
# expected =  [6,10,12]
# result = obj.findXSum(nums, k, x)
# printResult(result, expected)    

# nums = [3,8,7,8,7,5]
# k = 2
# x = 2
# expected =  [11,15,15,15,12]
# result = obj.findXSum(nums, k, x)
# printResult(result, expected)    
