from myUtils.Utils import printResult
from typing import List
import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        # print(frequencies)
        pq = []
        for _, val in frequencies.items():
            pq.append(-val)
        heapq.heapify(pq)

        time = 0
        while pq:
            cycle = n + 1
            tmp = []
            task_count = 0

            while cycle > 0 and pq:
                val = -heapq.heappop(pq)
                if val > 1:
                    tmp.append(-(val - 1))
                task_count += 1
                cycle -= 1

            for v in tmp:
                heapq.heappush(pq, v)

            if not pq:                
                time += task_count 
            else:
                time += n + 1

        return time


obj = Solution()

tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
expected = 8
result = obj.leastInterval(tasks, n)
printResult(result, expected)

tasks = ["A", "C", "A", "B", "D", "B"]
n = 1
expected = 6
result = obj.leastInterval(tasks, n)
printResult(result, expected)

tasks = ["A", "A", "A", "B", "B", "B"]
n = 3
expected = 10
result = obj.leastInterval(tasks, n)
printResult(result, expected)
