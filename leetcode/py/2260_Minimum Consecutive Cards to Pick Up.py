from typing import List
# You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # size = len(cards)
        lens = {}
        minDistance = 10**10
        for idx, card in enumerate(cards):
            if not card in lens:
                lens[card] = idx
                continue
            minDistance = min(minDistance, abs(idx - lens[card] + 1))
            lens[card] = idx
        # print(lens)
        if minDistance == 10**10:
            return -1
        return minDistance




obj = Solution()
print(obj.minimumCardPickup([3,4,2,3,4,7])) # 4
print(obj.minimumCardPickup([1,0,5,3])) # -1

# Example 1:

# Input: cards = [3,4,2,3,4,7]
# Output: 4
# Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
# Example 2:

# Input: cards = [1,0,5,3]
# Output: -1
# Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.