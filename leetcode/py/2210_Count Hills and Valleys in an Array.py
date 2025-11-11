from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        size = len(nums) - 1
        count = 0
        if size < 1:
            return count
        num = 0
        left = 0
        right = 0
        i = 1
        while i < size:
            left = nums[i - 1]
            right = nums[i + 1]
            num = nums[i]
            if right == num:
                future = 2
                if (i + future) <= size:
                    while num == nums[i + future] and i + future <= size:
                        future += 1
                        if (i + future) > size:
                            return count
                    right = nums[i + future]
                    i += future - 1
            # print("left: %s num: %s right: %s" %(left, num, right))
            if num > left and num > right:
                count += 1
            if num < left and num < right:
                count += 1
            i += 1

        return count

def printResult(result, expected):
    if result == expected:
        print("\033[92mpassed: %s result: %s expected: %s\033[0m" % (result == expected, result, expected))
    else:
        print("\033[91mpassed: %s result: %s expected: %s\033[0m" % (result == expected, result, expected))

obj = Solution()

# nums =  [2,4,1,1,6,5]
# expected = 3
# result = obj.countHillValley(nums)
# printResult(result, expected)

# nums =  [6,6,5,5,4,1]
# expected = 0
# result = obj.countHillValley(nums)
# printResult(result, expected)

nums = [57,57,57,57,57,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,85,85,85,86,86,86]
expected = 0
result = obj.countHillValley(nums)
printResult(result, expected)
