from myUtils.Utils import printResult
from typing import List

class Trie:

    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    def __str__(self):
        return f"Trie: children='{self.children}', isEndOfWord={self.isEndOfWord}"

    def __repr__(self):
        return self.__str__()
    
    def insert(self, word: str) -> None:
        current = self
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                current.children[c] = Trie()
                current = current.children[c]
        current.isEndOfWord = True
        # print(self)

    def search(self, word: str) -> bool:
        current = self
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                return False
        return current.isEndOfWord
        
    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return False
        return True
  
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Do not return anything, modify board in-place instead.
        """
        trie = Trie()
        for w in words:
            trie.insert(w)

        self.rows = len(board)
        self.cols = len(board[0])

        self.result = set()
        self.visited = set()

        def backtrack(r:int, c:int, node: Trie, path: str):
            if node.isEndOfWord:
                self.result.add(path)
            self.visited.add((r,c))

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0), ] # right, down, left, up
            for dirR, dirC in directions:
                newR, newC = r + dirR, c + dirC
                if 0 <= newR < self.rows and 0 <= newC < self.cols and (newR,newC) not in self.visited:
                    nextChar = board[newR][newC]
                    if nextChar in node.children:
                        backtrack(newR, newC, node.children[nextChar], path + nextChar)
            self.visited.remove((r,c))

        for r in range(self.rows):
            for c in range(self.cols):
                nextChar = board[r][c]
                if nextChar in trie.children:
                    backtrack(r, c, trie.children[nextChar], nextChar)

        res = list(self.result)
        res.sort()
        return res


obj = Solution()

board = [
    ["a","b","c"],
    ["a","e","d"],
    ["a","f","g"]
]
words = ["eaafgdcba", "eaabcdgfa"]
expected = ["eaabcdgfa","eaafgdcba"]
result = obj.findWords(board, words)
printResult(result, expected)

board = [["a","a"],["a","a"]]
words = ["aaaaa"]
expected = []
result = obj.findWords(board, words)
printResult(result, expected)

board = [
    ["a","b","c"],
    ["a","e","d"],
    ["a","f","g"]
]
words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
expected = ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]
result = obj.findWords(board, words)
printResult(result, expected)

board = [["a","b","c","e"],["x","x","c","d"],["x","x","b","a"]]
words = ["abc","abcd"]
expected = ["abc","abcd"]
result = obj.findWords(board, words)
printResult(result, expected)

board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"],
]
words = ["oath", "pea", "eat", "rain"]
expected = ["eat", "oath"]
result = obj.findWords(board, words)
printResult(result, expected)

board = [["a", "b"], ["c", "d"]]
words = ["abcb"]
expected = []
result = obj.findWords(board, words)
printResult(result, expected)

board = [["a", "b"], ["c", "d"]]
words = ["abdc"]
expected = ["abdc"]
result = obj.findWords(board, words)
printResult(result, expected)

board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]
expected = ["oa","oaa"]
result = obj.findWords(board, words)
printResult(result, expected)
