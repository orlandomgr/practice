class Solution:
    def maxDiff(self, num: int) -> int:
        maxN = num
        minN = num
        for x in range(10):
            for y in range(10):
                numS = str(num).replace(str(x), str(y))
                if numS[0] != "0":
                    numNew = int(numS)
                    minN = min(minN, numNew)    
                    maxN = max(maxN, numNew)    
        return maxN - minN

obj = Solution()
print(obj.maxDiff(555))
print(obj.maxDiff(9))
print(obj.maxDiff(123456))

