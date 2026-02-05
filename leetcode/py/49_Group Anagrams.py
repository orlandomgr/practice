from typing import List
from myUtils.Utils import printResult
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            # print(key)
            groups[key].append(word)
        # print(groups)
        return list(groups.values())
    
obj = Solution()

strs = ["",""]
expected = [["",""]]
result = obj.groupAnagrams(strs)
printResult(result, expected)

strs = ["eat","tea","tan","ate","nat","bat"]
expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
result = obj.groupAnagrams(strs)
printResult(result, expected)

strs = [""]
expected = [[""]]
result = obj.groupAnagrams(strs)
printResult(result, expected)

strs = ["a"]
expected = [["a"]]
result = obj.groupAnagrams(strs)
printResult(result, expected)
