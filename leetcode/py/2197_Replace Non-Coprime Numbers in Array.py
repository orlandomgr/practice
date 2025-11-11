from typing import List


class Solution:

    def getGCF(self, x: int, y: int) -> int:
        greater = x
        smaller = y
        if y > x:
            greater = y
            smaller = x

        result = 0
        while greater > 0:
            rem = greater % smaller

            if rem == 0:
                if result == 0:
                    result = smaller
                break
            else:
                greater = smaller
                smaller = rem
                result = rem
        # print("getGCF: x: %s y: %s result: %s" % (x, y, result))
        return result

    def getLCM(self, x: int, y: int, cfg: int) -> int:
        if cfg > 0:
            return int((x * y) / cfg)
        else:
            return 0

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        i = 0

        # print (nums)
        # for i in range(2):
        while i < len(nums) - 1:
            x = nums[i]
            y = nums[i + 1]
            if x == 1 or y == 1:
                i += 1
                continue
            gcf = self.getGCF(x, y)
            lcm = self.getLCM(x, y, gcf)
            # print("x: %s y: %s gcf: %s lcm: %s" % (x, y, gcf, lcm))
            if gcf > 1:
                nums[i] = lcm
                nums.pop(i + 1)
            else:
                i += 1

        i = len(nums) - 1
        while i > 0:
            # print(nums)
            x = nums[i]
            y = nums[i - 1]
            if x == 1 or y == 1:
                i -= 1
                continue
            gcf = self.getGCF(x, y)
            lcm = self.getLCM(x, y, gcf)
            # print("x: %s y: %s gcf: %s lcm: %s" % (x, y, gcf, lcm))
            if gcf > 1:
                nums[i] = lcm
                nums.pop(i - 1)
            i -= 1


        return nums


obj = Solution()
matrix = [6, 4, 3, 2, 7, 6, 2]
print(obj.replaceNonCoprimes(matrix))  # [12,7,6]

matrix = [2, 2, 1, 1, 3, 3, 3]
print(obj.replaceNonCoprimes(matrix))  # [2,1,1,3]

matrix = [517,11,121,517,3,51,3,1887,5]
print(obj.replaceNonCoprimes(matrix))  # [5687,1887,5]

matrix = [287,41,49,287,899,23,23,20677,5,825]
print(obj.replaceNonCoprimes(matrix))  # [2009,20677,825]
