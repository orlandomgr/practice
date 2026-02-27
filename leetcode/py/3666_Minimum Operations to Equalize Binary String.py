from myUtils.Utils import printResult
from collections import deque
from bisect import bisect_left, bisect_right

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count("0")

        if z == 0:
            return 0
        if n == k:
            if z == n:
                return 1
            if z == 0:
                return 0
            return -1

        even = list(range(0, n + 1, 2))
        odd = list(range(1, n + 1, 2))
        unvisited = [even, odd]
        if z in unvisited[z % 2]:
            unvisited[z % 2].remove(z)

        queue = deque([(z, 0)])
        while queue:
            cur, ops = queue.popleft()
            if cur == 0:
                return ops

            min_i = max(0, k - (n - cur))
            max_i = min(k, cur)
            z_min = cur + k - 2 * max_i
            z_max = cur + k - 2 * min_i

            next_parity = (cur + k) % 2
            lst = unvisited[next_parity]
            i = bisect_left(lst, z_min)
            j = bisect_right(lst, z_max)
            for z_next in lst[i:j]:
                queue.append((z_next, ops + 1))
            del lst[i:j]

        return -1

        
obj = Solution()

s = "110"
k = 1
expected = 1
result = obj.minOperations(s, k)
printResult(result, expected)

s = "0101"
k = 3
expected = 2
result = obj.minOperations(s, k)
printResult(result, expected)

s = "101"
k = 2
expected = -1
result = obj.minOperations(s, k)
printResult(result, expected)

s = "000100"
k = 2
expected = -1
result = obj.minOperations(s, k)
printResult(result, expected)

s = "0101101000100"
k = 7
expected = 2
result = obj.minOperations(s, k)
printResult(result, expected)

s = "01000011010111"
k = 8
expected = -1
result = obj.minOperations(s, k)
printResult(result, expected)

s = "11010000000011"
k = 6
expected = -1
result = obj.minOperations(s, k)
printResult(result, expected)

