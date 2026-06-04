from typing import List
from myUtils.Utils import printResult

"""
You are given two arrays of strings wordsContainer and wordsQuery.

For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.

Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].
"""
class Solution:    

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        class Node:
            __slots__ = ("children", "best_idx", "best_len")
            def __init__(self):
                self.children = {}
                self.best_idx = 0
                self.best_len = None

        root = Node()

        # Build trie of reversed container words. At each node store the best
        # candidate index among words that pass through that node. Best means
        # smallest length, then earliest index.
        for idx, w in enumerate(wordsContainer):
            node = root
            L = len(w)
            # update root best as all words share empty suffix
            if node.best_len is None or L < node.best_len or (L == node.best_len and idx < node.best_idx):
                node.best_len = L
                node.best_idx = idx
            for ch in reversed(w):
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
                if node.best_len is None or L < node.best_len or (L == node.best_len and idx < node.best_idx):
                    node.best_len = L
                    node.best_idx = idx

        result: List[int] = []
        for q in wordsQuery:
            node = root
            for ch in reversed(q):
                if ch in node.children:
                    node = node.children[ch]
                else:
                    break
            result.append(node.best_idx)
        return result


obj = Solution()

wordsContainer = ["abcd","bcd","xbcd"]
wordsQuery = ["cd","bcd","xyz"]
expected = [1,1,1]
result = obj.stringIndices(wordsContainer, wordsQuery)
printResult(result, expected)

wordsContainer = ["abcdefgh","poiuygh","ghghgh"]
wordsQuery = ["gh","acbfgh","acbfegh"]
expected = [2,0,2]
result = obj.stringIndices(wordsContainer, wordsQuery)
printResult(result, expected)

