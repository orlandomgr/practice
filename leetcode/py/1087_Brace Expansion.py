from myUtils.Utils import printResult
from typing import List


class Solution:
    def expandChar(self, c: str, sol: List[str]):
        # print("populate c: %s" %(c))
        if len(sol) == 0:
            sol.append(c)
        else:
            for i in range(len(sol)):
                sol[i] += c
        # print(sol)
        return sol
        
    def expandOptions(self, options: List[str], sol: List[str]):
        # print("options c: %s" %(options))
        if len(sol) == 0:
            for o in options:
                sol.append(o)
        else:
            extras = []
            while sol:
                opt = sol.pop(0)
                for o in options:
                    extras.append(opt + o)
            sol = extras
        # print(sol)
        return sol

    def expand(self, s: str) -> List[str]:
        sol = []
        n = len(s)
        idx = -1
        options = []
        exp = False
        while idx < n - 1:
            idx += 1
            c = s[idx]
            if c == ",":
                continue
            if c=='{':
                exp = True
                continue
            if c=='}':
                exp = False
                # print(options)
                sol = self.expandOptions(options, sol)
                options = []
                continue
            if exp:
                options.append(c)
            else:
                sol = self.expandChar(c, sol)
            
        # print(sol)
        sol.sort()
        return sol


obj = Solution()
s = "{a,b}c{d,e}f"
expected = ["acdf","acef","bcdf","bcef"]
result = obj.expand(s)
printResult(result, expected)

s = "abcd"
expected = ["abcd"]
result = obj.expand(s)
printResult(result, expected)
