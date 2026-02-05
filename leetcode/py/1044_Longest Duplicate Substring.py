from typing import List
from myUtils.Utils import printResult
from collections import defaultdict, Counter, OrderedDict
import heapq
from functools import cache
import re


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def calc(n):
            if not n:
                return True
            visited = set()
            for i in range(len(s) - n + 1):
                # print(s[i : i + n])
                if s[i : i + n] in visited:
                    self.ans = s[i : i + n]
                    return True
                visited.add(s[i : i + n])
            return False

        left = 0
        right = len(s) - 1
        self.ans = ""
        while left <= right:
            mid = (left + right) // 2
            if calc(mid):
                left = mid + 1
            else:
                right = mid - 1
        return self.ans

        # n = len(s)
        # res = ""
        # visited = set()

        # @cache
        # def isDuplicated(s, sub):
        #     indices = []
        #     start_index = 0
        #     while True:
        #         try:
        #             index = s.index(sub, start_index)
        #             indices.append(index)
        #             if len(indices) > 1:
        #                 return True
        #             start_index = index + 1
        #         except ValueError:
        #             break
        #     return len(indices) > 1

        # for i in range(n - 1, -1, -1):
        #     # times = n // i
        #     # print("new: %s times: %s" %(i, times))
        #     # print(f"\rsize: {i} words: {times}", end='', flush=True)
        #     if i == 0:
        #         break
        #     for j in range(0, n-i+1):
        #         word = s[j:j+i]
        #         if word in visited:
        #             continue
        #         visited.add(word)
        #         # print(word)
        #         if isDuplicated(s, word):
        #             if len(word) > len(res):
        #                 res = word
        #                 # print("\n")
        #                 return res
        # # print("\n")
        # return res


obj = Solution()

# s = "pmyiaxmicpmvqywlkisfzzutlxxjipitwcfxgqqfnxizowkqfmzsvkxryknasyvthozahbmapwqocupxcktmmtddxgatzftamrsvtddjpbnrojcqonmzxmknashplmykdbadiiccdkbyyzifqxvqfwgwihxgnrhqlmqprnjawuzcotutbkgnykuuwtzzzppmoyfmplhpznpnlwwbndekakpsmehzmbcfoyudgwsvehzgsfwqdkihiiwxfskicrbmoevxvpmmymihlkmgnuyohcofzfkehccwxezxypnnvqzrilr"
# expected = "knas"
# result = obj.longestDupSubstring(s)
# printResult(result, expected)

s = "moplvidmaagmsiyyrkchbyhivlqwqsjcgtumqscmxrxrvwsnjjvygrelcbjgbpounhuyealllginkitfaiviraqcycjmskrozcdqylbuejrgfnquercvghppljmojfvylcxakyjxnampmakyjbqgwbyokaybcuklkaqzawageypfqhhasetugatdaxpvtevrigynxbqodiyioapgxqkndujeranxgebnpgsukybyowbxhgpkwjfdywfkpufcxzzqiuglkakibbkobonunnzwbjktykebfcbobxdflnyzngheatpcvnhdwkkhnlwnjdnrmjaevqopvinnzgacjkbhvsdsvuuwwhwesgtdzuctshytyfugdqswvxisyxcxoihfgzxnidnfadphwumtgdfmhjkaryjxvfquucltmuoosamjwqqzeleaiplwcbbxjxxvgsnonoivbnmiwbnijkzgoenohqncjqnckxbhpvreasdyvffrolobxzrmrbvwkpdbfvbwwyibydhndmpvqyfmqjwosclwxhgxmwjiksjvsnwupraojuatksjfqkvvfroqxsraskbdbgtppjrnzpfzabmcczlwynwomebvrihxugvjmtrkzdwuafozjcfqacenabmmxzcueyqwvbtslhjeiopgbrbvfbnpmvlnyexopoahgmwplwxnxqzhucdieyvbgtkfmdeocamzenecqlbhqmdfrvpsqyxvkkyfrbyolzvcpcbkdprttijkzcrgciidavsmrczbollxbkytqjwbiupvsorvkorfriajdtsowenhpmdtvamkoqacwwlkqfdzorjtepwlemunyrghwlvjgaxbzawmikfhtaniwviqiaeinbsqidetfsdbgsydkxgwoqyztaqmyeefaihmgrbxzyheoegawthcsyyrpyvnhysynoaikwtvmwathsomddhltxpeuxettpbeftmmyrqclnzwljlpxazrzzdosemwmthcvgwtxtinffopqxbufjwsvhqamxpydcnpekqhsovvqugqhbgweaiheeicmkdtxltkalexbeftuxvwnxmqqjeyourvbdfikqnzdipmmmiltjapovlhkpunxljeutwhenrxyfeufmzipqvergdkwptkilwzdxlydxbjoxjzxwcfmznfqgoaemrrxuwpfkftwejubxkgjlizljoynvidqwxnvhngqakmmehtvykbjwrrrjvwnrteeoxmtygiiygynedvfzwkvmffghuduspyyrnftyvsvjstfohwwyxhmlfmwguxxzgwdzwlnnltpjvnzswhmbzgdwzhvbgkiddhirgljbflgvyksxgnsvztcywpvutqryzdeerlildbzmtsgnebvsjetdnfgikrbsktbrdamfccvcptfaaklmcaqmglneebpdxkvcwwpndrjqnpqgbgihsfeotgggkdbvcdwfjanvafvxsvvhzyncwlmqqsmledzfnxxfyvcmhtjreykqlrfiqlsqzraqgtmocijejneeezqxbtomkwugapwesrinfiaxwxradnuvbyssqkznwwpsbgatlsxfhpcidfgzrc"
expected = "akyj"
result = obj.longestDupSubstring(s)
printResult(result, expected)

# s = "aa"
# expected = "a"
# result = obj.longestDupSubstring(s)
# printResult(result, expected)

s = "banana"
expected = "ana"
result = obj.longestDupSubstring(s)
printResult(result, expected)

# s = "abcd"
# expected = ""
# result = obj.longestDupSubstring(s)
# printResult(result, expected)
