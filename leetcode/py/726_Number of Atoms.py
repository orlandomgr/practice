from typing import List
from myUtils.Utils import printResult
from collections import OrderedDict

class Solution:
    def getStringFromDict(self, dict:OrderedDict) -> str:
        s = []
        keys = list(dict.keys())
        keys.sort()
        for key in keys:
            val = dict[key]
            s.append(key)
            if val > 1:
                s.append(str(val))

        return "".join(s)

    def compute(self, s: str, multiplier: int) -> int:
        i = 0
        n = len(s)
        stack = []
        # print("compute: %s multiplier: %s" %(s, multiplier))
        while i < n:
            if s[i].isdigit():
                num = int(s[i])
                i += 1
                while i < n and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                stack.append(str(num))
            else:
                if s[i].islower():
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])
                i += 1

        # print(stack)
        tmp = OrderedDict()
        last = ""
        for item in stack:
            if item.isdigit():
                tmp[last] -= 1
                tmp[last] += int(item)
            else:
                if item not in tmp:
                    tmp[item] = 1
                else:
                    tmp[item] += 1

                last = item
        for key, val in tmp.items():
            tmp[key] *= multiplier                
        return tmp

    def countOfAtoms(self, formula: str) -> str:
        self.res = OrderedDict()

        formula = "".join(formula.split())
        # print(formula)
        left = formula.rfind("(")
        right = formula.find(")", left)
        n = len(formula)

        while left >= 0:
            multiplier = 1
            i = right + 1
            if i < n and formula[i].isdigit():
                num = int(formula[i])
                i += 1
                while i < n and formula[i].isdigit():
                    num = num * 10 + int(formula[i])
                    i += 1
                multiplier *= num
            
            val = self.compute(formula[left+1:right], multiplier)
            self.res.update(val)
            # print(val)
            if multiplier > 1:
                right += len(str(multiplier))
            formula = str(formula[:left]) + self.getStringFromDict(val) + str(formula[right+1:])
            left = formula.rfind("(")
            right = formula.find(")", left)
            n = len(formula)
        val = self.compute(formula, 1)
        self.res.update(val)
        
        # print(self.res)

        return self.getStringFromDict(self.res)
    
obj = Solution()

formula = "Mg(H2O)"
expected = "H2MgO"
result = obj.countOfAtoms(formula)
printResult(result, expected)

formula = "H2O"
expected = "H2O"
result = obj.countOfAtoms(formula)
printResult(result, expected)

formula = "Mg(OH)2"
expected = "H2MgO2"
result = obj.countOfAtoms(formula)
printResult(result, expected)

formula = "K4(ON(SO3)2)2"
expected = "K4N2O14S4"
result = obj.countOfAtoms(formula)
printResult(result, expected)


