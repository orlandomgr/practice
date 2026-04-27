from typing import List
from myUtils.Utils import printResult
from collections import Counter
"""
You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.

In the ith move, you can choose one of the following directions:

move to the left if moves[i] = 'L' or moves[i] = '_'
move to the right if moves[i] = 'R' or moves[i] = '_'
Return the distance from the origin of the furthest point you can get to after n moves.
"""
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        result = 0
        counter = Counter(moves).most_common(2)
        newC = None
        for c,_ in counter:
            if c == "_":
                continue
            if c == "L":
                newC = "L"
                break
            else:
                newC = "R"
                break
        print(counter)
        print(newC)
        if not newC:
            newC = "R"
        moves = moves.replace("_", newC)
        print(counter)
        print(newC)
        for c in moves:
            if c == "L":
                result -= 1
            elif c == "R":
                result += 1
            # else:
            #     if abs(result - 1) > result:
            #         result -= 1
            #     else:
            #         result += 1
        return abs(result)
            
obj = Solution()

moves = "LLR_"
expected = 2
result = obj.furthestDistanceFromOrigin(moves)
printResult(result, expected)

# moves = "L_RL__R"
# expected = 3
# result = obj.furthestDistanceFromOrigin(moves)
# printResult(result, expected)

# moves = "_R__LL_"
# expected = 5
# result = obj.furthestDistanceFromOrigin(moves)
# printResult(result, expected)

# moves = "_______"
# expected = 7
# result = obj.furthestDistanceFromOrigin(moves)
# printResult(result, expected)
