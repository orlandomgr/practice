from typing import List
from myUtils.Utils import printResult
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        counter = Counter(nums)
        mostCommon = counter.most_common()
        count = 0
        # print(mostCommon)
        for num, _ in mostCommon:
            res.append(num)
            count += 1
            if count >= k:
                break

        return res


obj = Solution()

nums = [1, 1, 1, 2, 2, 3]
k = 2
expected = [1, 2]
result = obj.topKFrequent(nums, k)
printResult(result, expected)

nums = [1]
k = 1
expected = [1]
result = obj.topKFrequent(nums, k)
printResult(result, expected)

nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2]
k = 2
expected = [1, 2]
result = obj.topKFrequent(nums, k)
printResult(result, expected)
