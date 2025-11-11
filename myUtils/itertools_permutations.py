from typing import List
import itertools

def getPermutations(options: List[int]) -> List[List[int]]:
    if len(options) == 0:
        return [[]]
    if len(options) == 1:
        return [[options[0]]]

    permutations = []
    for i in range(len(options)):
        pending = options[:i] + options[i+1:]
        pendingPermutations = getPermutations(pending)
        for p in pendingPermutations:
            permutations.append([options[i]] + p)
    return permutations

# print(getPermutations([1,2,3]))
print(getPermutations(["a","b","b","c"]))

# for p in itertools.permutations([1,2,3]):
#     print(p)