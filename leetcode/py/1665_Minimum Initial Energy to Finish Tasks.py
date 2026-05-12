from typing import List
from myUtils.Utils import printResult

"""
You are given an array tasks where tasks[i] = [actuali, minimumi]:

actuali is the actual amount of energy you spend to finish the ith task.
minimumi is the minimum amount of energy you require to begin the ith task.
For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

You can finish the tasks in any order you like.

Return the minimum initial amount of energy you will need to finish all the tasks.
"""

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        initial_energy = 0
        current_energy = 0

        for actual, minimum in tasks:
            if current_energy < minimum:
                initial_energy += minimum - current_energy
                current_energy = minimum
            current_energy -= actual

        return initial_energy

obj = Solution()

tasks = [[1,2],[2,4],[4,8]]
expected = 8
result = obj.minimumEffort(tasks)
printResult(result, expected)

tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
expected = 32
result = obj.minimumEffort(tasks)
printResult(result, expected)

tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
expected = 27
result = obj.minimumEffort(tasks)
printResult(result, expected)

