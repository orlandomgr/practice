from myUtils.Utils import printResult
import random

class RandomizedSet:

    def __init__(self):
        self.mySet = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        # print("insert: %s from: %s" %(val, self.mySet))
        if val in self.idx:
            return False
        
        self.mySet.append(val)
        self.idx[val] = len(self.mySet) - 1
        return True

    def remove(self, val: int) -> bool:
        # print("remove: %s from: %s" %(val, self.mySet))
        if val not in self.idx:
            return False

        i = self.idx[val]
        self.mySet.remove(val)
        # del self.mySet[i]
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        # print("random: %s" %self.mySet)
        return random.choice(self.mySet)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

randomizedSet = RandomizedSet()
result = randomizedSet.insert(1) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
printResult(result, True)        
result = randomizedSet.remove(2) # Returns false as 2 does not exist in the set.
printResult(result, False)        
result = randomizedSet.insert(2) # Inserts 2 to the set, returns true. Set now contains [1,2].
printResult(result, True)        
result = randomizedSet.getRandom() # getRandom() should return either 1 or 2 randomly.
result = result == 1 or result == 2
printResult(result, True)
result = randomizedSet.remove(1) # Removes 1 from the set, returns true. Set now contains [2].
printResult(result, True)
result = randomizedSet.insert(2) # 2 was already in the set, so return false.
printResult(result, False)
result = randomizedSet.getRandom() # Since 2 is the only number in the set, getRandom() will always return 2.
printResult(result, 2)
