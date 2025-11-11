from typing import List
from myUtils.Utils import printResult
from functools import cache

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for o in operations:
            if o.find("++") > -1:
              result += 1                
            else:
              result -= 1                
        return result

obj = Solution()

operations=["--X","X++","X++"]
expected = 1
result = obj.finalValueAfterOperations(operations)
printResult(result, expected)

operations=["++X","++X","X++"]
expected = 3
result = obj.finalValueAfterOperations(operations)
printResult(result, expected)

operations=["X++","++X","--X","X--"]
expected = 0
result = obj.finalValueAfterOperations(operations)
printResult(result, expected)

