from typing import List

# On day 1, one person discovers a secret.

# You are given an integer delay, which means that each person will share the secret with a new person every day, starting from delay days after discovering the secret. You are also given an integer forget, which means that each person will forget the secret forget days after discovering it. A person cannot share the secret on the same day they forgot it, or on any day afterwards.

# Given an integer n, return the number of people who know the secret at the end of day n. Since the answer may be very large, return it modulo 109 + 7.


class Solution:

    def swapPeople(self, days: List[int]):
        # del days[len(days)-1]
        # days.insert(0, 0)
        # return days
        return [0] + days[0:-1]
        # current = 0
        # prev = 0
        # for idx, value in enumerate(days):
        #     current = days[idx]
        #     days[idx] = prev
        #     prev = current
        # return days

    def shareSecret(self, days: List[int], delay: int):
        total = 0
        # for idx, value in enumerate(days):
        #     if idx < delay or idx == len(days) - 1:
        #         continue
        #     total += days[idx]
        # days[0] += total
        # sum(days[delay:])
        days[0] += sum(days[delay:-1])

        return days

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        days = [0] * (forget + 1)

        days[0] = 1
        for d in range(n):
            # [0] + days[0:-1] swap
            # sum(days[delay+1:-1]) share
            days = [sum(days[delay-1:-2])] + days[0:-1]
            print(days)
            # days = self.swapPeople(days)
            # days = self.shareSecret(days, delay)
            # days = [0] + days[0:-1]
            # days[0] = sum(days[delay:-1])

        # total = 0
        # for idx, value in enumerate(days):
        #     if idx == 0:
        #         continue
        #     total += value

        total = sum(days[1:])
        print(days)


        if total > 10**9:
            total = total % (10**9 + 7)
        return total



obj = Solution()
# print(obj.peopleAwareOfSecret(6, 2, 4))  # 5
# print(obj.peopleAwareOfSecret(4, 1, 3))  # 6
# print(obj.peopleAwareOfSecret(684, 18, 496))  # 653668527
# print(obj.peopleAwareOfSecret(678, 100, 247))  # 6155841149


# Input: n = 4, delay = 1, forget = 3
# Output: 6
# Explanation:
# Day 1: The first person is named A. (1 person)
# Day 2: A shares the secret with B. (2 people)
# Day 3: A and B share the secret with 2 new people, C and D. (4 people)
# Day 4: A forgets the secret. B, C, and D share the secret with 3 new people. (6 people)


# Example 1:

# Input: n = 6, delay = 2, forget = 4
# Output: 5
# Explanation:
# Day 1: Suppose the first person is named A. (1 person)
# Day 2: A is the only person who knows the secret. (1 person)
# Day 3: A shares the secret with a new person, B. (2 people)
# Day 4: A shares the secret with a new person, C. (3 people)
# Day 5: A forgets the secret, and B shares the secret with a new person, D. (3 people)
# Day 6: B shares the secret with E, and C shares the secret with F. (5 people)
# Example 2:
