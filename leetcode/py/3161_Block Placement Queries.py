from typing import List
from myUtils.Utils import printResult
import random

"""
There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

You are given a 2D array queries, which contains two types of queries:

For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.
"""

random.seed(0)

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (2 * size)

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            self.tree[i >> 1] = max(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l, r):
        res = 0
        l += self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l >>= 1
            r >>= 1
        return res


class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (size + 1)
        self.bits = size.bit_length()

    def add(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def find_kth(self, k):
        idx = 0
        for i in range(self.bits, -1, -1):
            next_idx = idx + (1 << i)
            if next_idx <= self.n:
                if self.tree[next_idx] < k:
                    k -= self.tree[next_idx]
                    idx = next_idx
        return idx + 1


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        # Dynamically set size based on maximum coordinate in queries (with a safe default of 50005)
        max_coord = max(q[1] for q in queries)
        MAX_VAL = max(50005, max_coord + 5)
        
        st = SegmentTree(MAX_VAL)
        bit = FenwickTree(MAX_VAL)
        
        # Obstacle at 0 (implicit). 1-based indexing for Fenwick Tree is x + 1.
        bit.add(1, 1)
        total_obstacles = 1
        
        results = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                cnt = bit.query(x + 1)
                
                # Predecessor of x
                prev_idx = bit.find_kth(cnt)
                prev = prev_idx - 1
                
                # Successor of x
                if cnt < total_obstacles:
                    nxt_idx = bit.find_kth(cnt + 1)
                    nxt = nxt_idx - 1
                    st.update(nxt, nxt - x)
                
                st.update(x, x - prev)
                bit.add(x + 1, 1)
                total_obstacles += 1
            else:
                _, x, sz = q
                if sz > x:
                    results.append(False)
                    continue
                
                cnt = bit.query(x + 1)
                prev_idx = bit.find_kth(cnt)
                prev = prev_idx - 1
                
                max_gap = max(st.query(0, x), x - prev)
                results.append(max_gap >= sz)
                
        return results


obj = Solution()

queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
expected =  [False,True,True]
result = obj.getResults(queries)
printResult(result, expected)

obj = Solution()
queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
expected = [True,True,False]
result = obj.getResults(queries)
printResult(result, expected)
