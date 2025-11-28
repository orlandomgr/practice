from myUtils.Utils import printResult
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity        
        self.cache =  OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
expected = 1
result = lRUCache.get(1)    # return 1
printResult(result, expected)           
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
expected = -1
result = lRUCache.get(2)    # returns -1 (not found)
printResult(result, expected)           
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
expected = -1
result = lRUCache.get(1)    # return -1 (not found)
printResult(result, expected)           
expected = 3
result = lRUCache.get(3)    # return 3
printResult(result, expected)           
expected = 4
result = lRUCache.get(4)    # return 4
printResult(result, expected)           
