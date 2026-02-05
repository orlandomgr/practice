from myUtils.Utils import printResult
import bisect 

class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.array, num) 

    def findMedian(self) -> float:
        n = len(self.array)
        mid = n // 2
        # print(self.array)
        if n % 2 == 1:
            return self.array[mid]
        else:
            s = self.array[mid-1] + self.array[mid]
            return s / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(1);    # arr = [1]
# obj.addNum(2);    # arr = [1, 2]
# result = obj.findMedian(); # return 1.5 (i.e., (1 + 2) / 2)
# expected = 1.5
# printResult(result, expected)
# obj.addNum(3);    # arr[1, 2, 3]
# result = obj.findMedian(); # return 1.5 (i.e., (1 + 2) / 2)
# expected = 2.0
# printResult(result, expected)

obj = MedianFinder()

obj.addNum(6)
result = obj.findMedian()
expected = 6.0
printResult(result, expected)

obj.addNum(10)
result = obj.findMedian()
expected = 8.0
printResult(result, expected)

obj.addNum(2)
result = obj.findMedian()
expected = 6.0
printResult(result, expected)

obj.addNum(6)
result = obj.findMedian()
expected = 6.0
printResult(result, expected)

obj.addNum(5)
result = obj.findMedian()
expected = 6.0
printResult(result, expected)

obj.addNum(0)
result = obj.findMedian()
expected = 5.5
printResult(result, expected)

obj.addNum(6)
result = obj.findMedian()
expected = 6.0
printResult(result, expected)

obj.addNum(3)
result = obj.findMedian()
expected = 5.5
printResult(result, expected)

obj.addNum(1)
result = obj.findMedian()
expected = 5.0
printResult(result, expected)

obj.addNum(0)
result = obj.findMedian()
expected = 4.0
printResult(result, expected)

obj.addNum(0)
result = obj.findMedian()
expected = 3.0
printResult(result, expected)
