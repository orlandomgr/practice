from typing import List
import heapq


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # self.counter = itertools.count()
        self.processes = []
        self.processFinder = {}
        heapq.heapify(self.processes)
        for userId, taskId, priority in tasks:
            # print("userId: %s taskId: %s priority: %s" % (userId, taskId, priority))
            entry = self.getEntry(priority, taskId, userId)
            self.processFinder[taskId] = entry
            heapq.heappush(self.processes, entry)
        # print(self.processes)

    def getEntry(self, priority: int, taskId: int, userId: int):
        entry = [-priority, -taskId, str(userId)] # , next(self.counter)
        return entry

    def add(self, userId: int, taskId: int, priority: int) -> None:
        entry = self.getEntry(priority, taskId, userId)
        self.processFinder[taskId] = entry
        heapq.heappush(self.processes, entry)

    def markRemoved(self, entry):
        # entry[0] = 1
        # entry[1] = "removed"
        entry[2] = "removed"
        # entry = None
        return entry

    def edit(self, taskId: int, newPriority: int) -> None:
        entry = self.processFinder[taskId]
        newEntry = self.getEntry(newPriority, -entry[1], entry[2])
        entry = self.markRemoved(entry)
        self.processFinder[taskId] = newEntry
        heapq.heappush(self.processes, newEntry)

    def rmv(self, taskId: int) -> None:
        entry = self.processFinder[taskId]
        entry = self.markRemoved(entry)

    def execTop(self) -> int:
        entry = None
        # print(self.processes)
        if len(self.processes) > 0:
            entry = heapq.heappop(self.processes)
            while entry[2] == "removed":
                if len(self.processes) > 0:
                    entry = heapq.heappop(self.processes)
                else:
                    entry = None
                    break

            # print(self.processes)
            # print(entry[2])
        if entry is not None:
            return int(entry[2])
        else:
            return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()


taskManager = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
# Initializes with three tasks for Users 1, 2, and 3.
taskManager.add(4, 104, 5); # Adds task 104 with priority 5 for User 4.
taskManager.edit(102, 8); # Updates priority of task 102 to 8.
taskManager.execTop(); # return 3. Executes task 103 for User 3.
taskManager.rmv(101); # Removes task 101 from the system.
taskManager.add(5, 105, 15); # Adds task 105 with priority 15 for User 5.
taskManager.execTop(); # return 5. Executes task 105 for User 5.


# taskManager = TaskManager([[3,12,11],[6,2,46],[2,1,46],[5,23,21]])
# taskManager.execTop()

# [[[[3,12,11],[6,2,46],[2,1,46],[5,23,21]]],[]]

# taskManager = TaskManager([[10,26,25]])
# taskManager.rmv(26)
# taskManager.execTop()

# taskManager = TaskManager([[8,17,33],[4,14,42]])
# taskManager.edit(14, 21)
# taskManager.execTop()


# taskManager = TaskManager([[1,101,10],[2,102,20],[3,103,15]])
# taskManager.add(4,104,5)
# taskManager.edit(102, 8)
# taskManager.execTop()
# taskManager.rmv(101)
# taskManager.add(5,105,15)
# taskManager.execTop()

# taskManager = TaskManager([[5,5,14],[5,20,4],[10,12,5]])
# taskManager.rmv(20)
# taskManager.add(6,0,22)
# taskManager.add(9,20,13)
# taskManager.execTop()

# taskManager = TaskManager([[6,3,1],[8,19,29],[10,7,25],[2,9,41],[1,16,27],[9,0,48],[7,25,39],[7,26,16],[10,12,18],[4,20,2]])
# taskManager.rmv(0)
# taskManager.rmv(9)
# taskManager.execTop()
# taskManager.execTop()

taskManager = TaskManager([[1,101,8],[2,102,20],[3,103,5]])
taskManager.add(4,104,5)
taskManager.edit(102,9)
taskManager.execTop()
taskManager.rmv(101)
taskManager.add(50,101,8)
taskManager.execTop()
