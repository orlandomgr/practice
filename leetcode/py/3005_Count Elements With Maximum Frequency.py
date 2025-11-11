from typing import List

# You are given an array nums consisting of positive integers.

# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

# The frequency of an element is the number of occurrences of that element in the array.

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = {}

        maxCount = 0
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1
            maxCount = max(maxCount, frequencies[num])

        if maxCount == 1:
            return len(nums)

        count = 0
        for freq in frequencies.values():
            if freq == maxCount:
                count += 1
                # print(freq)

        return count * maxCount 
        

obj = Solution()
array = [1,2,2,3,1,4]        
expected = 4
result = obj.maxFrequencyElements(array)
print(result)
print(result == expected)

array = [1,2,3,4,5]
expected = 5
result = obj.maxFrequencyElements(array)
print(result)
print(result == expected)
