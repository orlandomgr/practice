from myUtils.Utils import printResult

class Trie:

    def __init__(self):
        self.children = {}
        self.isWord = False

    def __str__(self):
        return f"Trie: children='{self.children}', isWord={self.isWord}"

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
        current.isWord = True
        # print(self)

    def search(self, word: str) -> bool:
        current = self
        for c in word:
            if c in current.children:
                current = current.children[c]
            else:
                return False
        return current.isWord
        
    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            if c in current.children:
                current = current.children[c]
            else:
                return False
        return True
     

trie = Trie()
trie.insert("apple")
result = trie.search("apple")   # return True
printResult(result, True)
result = trie.search("app")     # return False
printResult(result, False)
result = trie.startsWith("app") # return True
printResult(result, True)
trie.insert("app")
result = trie.search("app")     # return True
printResult(result, True)
