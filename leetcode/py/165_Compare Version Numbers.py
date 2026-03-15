# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        while len(ver1) > 0 or len(ver2) > 0:
            v1 = 0
            if len(ver1) > 0:
                v1 = int(ver1.pop(0))

            v2 = 0
            if len(ver2) > 0:
                v2 = int(ver2.pop(0))

            # print("v1: %s v2: %s" %(v1, v2))

            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0


obj = Solution()
print(obj.compareVersion("1.2", "1.10")) # -1
print(obj.compareVersion("1.01", "1.001")) # 0
print(obj.compareVersion("1.0", "1.0.0.0")) # 0
