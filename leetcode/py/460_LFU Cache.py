from myUtils.Utils import printResult
from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minCounter = 0
        self.keyToValue = {}
        self.keyToCounter = {}
        self.counterToKeys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        # print(self.cacheFinder)
        if key not in self.keyToValue:
            return -1
        
        counter = self.keyToCounter[key]
        value = self.keyToValue[key]

        del self.counterToKeys[counter][key]

        if not self.counterToKeys[counter]:
            del self.counterToKeys[counter]
            if counter == self.minCounter:
                self.minCounter += 1

        self.counterToKeys[counter + 1][key] = None
        self.keyToCounter[key] = counter + 1
        return value

    def put(self, key: int, value: int) -> None:
        # print("put key: %s value: %s cache: %s" %(key, value, self.cache))
        if self.capacity == 0:
            return
        if key in self.keyToValue:
            self.keyToValue[key] = value
            self.get(key)
            return 

        if len(self.keyToValue) == self.capacity:
            keyToDelete, _ = self.counterToKeys[self.minCounter].popitem(last=False)
            del self.keyToValue[keyToDelete]
            del self.keyToCounter[keyToDelete]

        self.keyToValue[key] = value
        self.keyToCounter[key] = 1
        self.counterToKeys[1][key] = None
        self.minCounter = 1


lfu = LFUCache(3)
lfu.put(2, 2)  
lfu.put(1, 1)  
result = lfu.get(2)
printResult(result, 2) 
result = lfu.get(1)
printResult(result, 1) 
result = lfu.get(2)
printResult(result, 2) 
lfu.put(3, 3)  
lfu.put(4, 4)  
result = lfu.get(3)
printResult(result, -1) 
result = lfu.get(2)
printResult(result, 2) 
result = lfu.get(1)
printResult(result, 1) 
result = lfu.get(4)
printResult(result, 4) 


lfu = LFUCache(2)
lfu.put(2, 1)  
lfu.put(3, 2)  
result = lfu.get(3)
printResult(result, 2) 
result = lfu.get(2)
printResult(result, 1) 
lfu.put(4, 3)  
result = lfu.get(2)
printResult(result, 1) 
result = lfu.get(3)
printResult(result, -1) 
result = lfu.get(4)
printResult(result, 3) 


lfu = LFUCache(2)
lfu.put(3, 1)
lfu.put(2, 1)
lfu.put(2, 2)
lfu.put(4, 4)
result = lfu.get(2)
printResult(result, 2) 

lfu = LFUCache(2)
lfu.put(1, 1)   
lfu.put(2, 2)   
result = lfu.get(1)
printResult(result, 1) 
lfu.put(3, 3)   
result = lfu.get(2)
printResult(result, -1) 
result = lfu.get(3)
printResult(result, 3) 
lfu.put(4, 4)   
result = lfu.get(1)
printResult(result, -1) 
result = lfu.get(3)
printResult(result, 3) 
result = lfu.get(4)
printResult(result, 4) 
