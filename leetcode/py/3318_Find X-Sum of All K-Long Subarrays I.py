from typing import List
from myUtils.Utils import printResult
from collections import Counter

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
        for i in range(n - k + 1):
            # print(nums[i:i+k])
            result.append(self.xSum(nums[i:i+k], x))
        return result
    
obj = Solution()

nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2
expected =  [6,10,12]
result = obj.findXSum(nums, k, x)
printResult(result, expected)    

nums = [3,8,7,8,7,5]
k = 2
x = 2
expected =  [11,15,15,15,12]
result = obj.findXSum(nums, k, x)
printResult(result, expected)    
