from typing import List


class Solution:
    def hIndexR(self, citations: List[int], start: int, end: int, mid: int, h: int) -> int:
        size = end + start
        mid = size // 2
        print("hIndexR: citations: %s h: %s mid: %s start: %s end: %s" % (citations, h, mid, start, end))
        if size <= 0 or start < 0 or end > len(citations) or end < start:
            return h
        
        if citations[-mid] >= mid:
            return self.hIndexR(citations, mid + 1, end, mid, mid)
        else:
            return self.hIndexR(citations, start, mid - 1, mid, h)

    def hIndex(self, citations: List[int]) -> int:
        return self.hIndexR(citations, 0, len(citations), 0, 0)


obj = Solution()
print(obj.hIndex([0]))  # 0
print(obj.hIndex([0, 1, 3, 5, 6]))  # 3
print(obj.hIndex([1, 2, 100]))  # 2
print(obj.hIndex([2, 4, 5, 5, 6, 7, 8]))  # 5
