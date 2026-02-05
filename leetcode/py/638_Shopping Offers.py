from typing import List
from myUtils.Utils import printResult
from collections import deque


class Solution:
    def filterSpecials(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ):
        special.sort()
        newSpecial = []
        i = 1
        n = len(special)
        while i < n:
            s1 = special[i-1]
            s2 = special[i]

            if s1[:-1] == s2[:-1]:
                if s1[-1] < s2[-1]:
                    special.remove(s2)
                    n = len(special)
                    continue
            i += 1

        for s in special:
            drop = False
            p = 0
            for i in range(len(s) - 1):
                p += s[i] * price[i]
                if s[i] > needs[i]:
                    drop = True
                    break
            # print(p)
            # print(s[-1])
            if p < s[-1]:
                drop = True
            if not drop:
                newSpecial.append(s)
        return newSpecial

    def dfs(self, price: List[int], special: List[List[int]], needs: List[int]):

        q = deque()
        q.append((needs, 0))

        results = []
        results.append((needs,0))
        while q:
            # print(q)
            needs, cost = q.popleft()

            for s in special:
                drop = False
                for i in range(len(s) - 1):
                    if s[i] > needs[i]:
                        drop = True
                        break
                if not drop:
                    newNeeds = needs[:]
                    for i in range(len(s) - 1):
                        newNeeds[i] -= s[i]
                    q.append((newNeeds, cost + s[-1]))
                else:
                    results.append((needs, cost))

        lowestCost = 10**10
        for i in range(len(results)):
            needs = results[i][0]
            cost = results[i][1]
            for i in range(len(needs)):
                cost += needs[i] * price[i]
            lowestCost = min(lowestCost, cost)

        return lowestCost

    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        totalCost = 0
        special = self.filterSpecials(price, special, needs)
        # print(special)
        totalCost = self.dfs(price, special, needs)
        return totalCost


obj = Solution()

price = [2,2]
special = [[1,1,1],[1,1,2],[1,1,3],[1,1,4],[1,1,5],[1,1,6],[1,1,7],[1,1,8],[1,1,9],[1,1,10],[1,1,11],[1,1,12],[1,1,13],[1,1,14],[1,1,15]]
needs = [10, 10]
expected = 10
result = obj.shoppingOffers(price, special, needs)
printResult(result, expected)

# price = [3, 4]
# special = [[1, 2, 3], [1, 2, 5]]
# needs = [2, 2]
# expected = 6
# result = obj.shoppingOffers(price, special, needs)
# printResult(result, expected)

# price = [0, 0, 0]
# special = [[1, 1, 0, 4], [2, 2, 1, 9]]
# needs = [1, 1, 1]
# expected = 0
# result = obj.shoppingOffers(price, special, needs)
# printResult(result, expected)

# price = [2, 5]
# special = [[3, 0, 5], [1, 2, 10]]
# needs = [3, 2]
# expected = 14
# result = obj.shoppingOffers(price, special, needs)
# printResult(result, expected)

# price = [2, 3, 4]
# special = [[1, 1, 0, 4], [2, 2, 1, 9]]
# needs = [1, 2, 1]
# expected = 11
# result = obj.shoppingOffers(price, special, needs)
# printResult(result, expected)
