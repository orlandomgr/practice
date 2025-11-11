from typing import List 

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i in range(len(words)):
            if x in words[i]:
                result.append(i)
            # if words[i].find(x) != -1:
            #     result.append(i)

        return result
    
obj = Solution()

words = ["leet","code"]
x = "e"
expected = [0,1]
result = obj.findWordsContaining(words, x)    
print("passed: %s result: %s" %(result == expected, result))

words = ["abc","bcd","aaaa","cbc"]
x = "a"
expected = [0,2]
result = obj.findWordsContaining(words, x)    
print("passed: %s result: %s" %(result == expected, result))

words = ["abc","bcd","aaaa","cbc"]
x = "z"
expected = []
result = obj.findWordsContaining(words, x)    
print("passed: %s result: %s" %(result == expected, result))

