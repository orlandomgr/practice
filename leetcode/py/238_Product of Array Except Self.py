from typing import List
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size
        prefix = [1] *  size
        postfix = [1] * size
        current1 = nums[0]
        current2 = nums[size - 1]
        for idx, n in enumerate(nums):
            if idx == 0:
                continue
            prefix[idx] = current1
            current1 *= n

            postfix[size - 1 - idx] = current2
            current2 *= nums[size - 1 - idx]

        for i in range(size):
            result[i] = prefix[i] * postfix[i]

        # print(prefix)
        # print(postfix)
        # print(result)
        return result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [1] * size
        prefix = 1
        suffix = 1
        for i in range(size):
            result[i] *= prefix
            prefix *= nums[i]
        for j in range(size - 1, -1, -1):
            result[j] *= suffix
            suffix *= nums[j]
        return result

obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))
# print(obj.productExceptSelf([-1, 1, 0, -3, 3]))


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
