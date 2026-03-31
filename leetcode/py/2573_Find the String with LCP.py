from typing import List
from myUtils.Utils import printResult

"""
We define the lcp matrix of any 0-indexed string word of n lowercase English letters as an n x n grid such that:

lcp[i][j] is equal to the length of the longest common prefix between the substrings word[i,n-1] and word[j,n-1].
Given an n x n matrix lcp, return the alphabetically smallest string word that corresponds to lcp. If there is no such string, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "aabd" is lexicographically smaller than "aaca" because the first position they differ is at the third letter, and 'b' comes before 'c'.
"""
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py
        
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)
        
        groups = {}
        for i in range(n):
            root = find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)
        
        if len(groups) > 26:
            return ""
        
        word = [""] * n
        current = ord("a")
        # Sort groups by the smallest index in each group to assign smallest letters to earliest positions
        sorted_groups = sorted(groups.items(), key=lambda x: min(x[1]))
        for root, indices in sorted_groups:
            letter = chr(current)
            for idx in indices:
                word[idx] = letter
            current += 1
        
        # Verification
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i == n - 1 or j == n -1:
                        if lcp[i][j] != 1:
                            return ""
                    else:
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""
                else:
                    if lcp[i][j] != 0:
                        return ""
        
        return "".join(word)


obj = Solution()

lcp = [[4,0,2,0],[0,3,0,1],[2,0,2,0],[0,1,0,1]]
expected = "abab"
result = obj.findTheString(lcp)
printResult(result, expected)

lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
expected = "aaaa"
result = obj.findTheString(lcp)
printResult(result, expected)

lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,3]]
expected = ""
result = obj.findTheString(lcp)
printResult(result, expected)

lcp = [[9,1,0,1,0,1,0,0,1],[1,8,0,4,0,2,0,0,1],[0,0,7,0,3,0,1,2,0],[1,4,0,6,0,2,0,0,1],[0,0,3,0,5,0,1,2,0],[1,2,0,2,0,4,0,0,1],[0,0,1,0,1,0,3,1,0],[0,0,2,0,2,0,1,2,0],[1,1,0,1,0,1,0,0,1]]
expected = "aabababba"
result = obj.findTheString(lcp)
printResult(result, expected)
