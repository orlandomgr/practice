from typing import List
import itertools

def getCombinations(options: List, size: int) -> List[List[int]]:
    if size == 0:
        return [[]]
    if not options:
        return []

    first = options[0]
    pending = options[1:]

    combinationsWithFirst = []
    combinationsWithOutFirst = []

    for combo in getCombinations(pending, size -1):
        combinationsWithFirst.append([first] + combo)
    combinationsWithOutFirst = getCombinations(pending, size )
    return combinationsWithFirst + combinationsWithOutFirst

print(getCombinations([1,2,3], 2))
# print(getCombinations(["a", "b", "c", "d"], 3))

for combo in itertools.combinations([1,2,3], 2):
    print(combo)

# print(itertools.combinations([1,2,3], 3))