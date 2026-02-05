from typing import List
from myUtils.Utils import printResult
from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        self.data = {}
        for i in range(length):
            innerList = defaultdict(int)
            innerList.setdefault(0, 0)
            self.data.setdefault(i, innerList)
        self.snapId = 0

    def set(self, index: int, val: int) -> None:
        if index < len(self.data):
            self.data[index][self.snapId] = val        

    def snap(self) -> int:
        # for data in self.data:
        #     data.append(data[-1])
        self.snapId += 1
        return self.snapId - 1

    def get(self, index: int, snap_id: int) -> int:
        # print(self.data)
        if index < len(self.data) and snap_id < self.snapId:
            innerList = self.data[index]
            if snap_id not in innerList:
                while snap_id > 0:
                    if snap_id in innerList:
                        break
                    snap_id -= 1
            
            return self.data[index][snap_id]
        else:
            return -1
        

obj = SnapshotArray(3)
obj.set(0,5)
printResult(obj.snap(), 0)
obj.set(0,6)
printResult(obj.get(0, 0), 5)