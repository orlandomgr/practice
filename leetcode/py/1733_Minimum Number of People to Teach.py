from typing import List
# On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

# You are given an integer n, an array languages, and an array friendships where:

# There are n languages numbered 1 through n,
# languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
# friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
# You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

# Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang = {}
        for idx, val in enumerate(languages):
            lang.setdefault(idx + 1, set()).update(val)

        p = set()
        for u1, u2 in friendships:
            if lang[u1].isdisjoint(lang[u2]):
                p.add(u1)
                p.add(u2)

        result = 10**10
        for i in range(n + 1):
            counter = 0
            for user in p:
                if i in lang[user]:
                    counter += 1
            result = min(result, len(p) - counter) 

        print(lang)
        print(p)
        return result

obj = Solution()
# print(obj.minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]])) # 1
# print(obj.minimumTeachings(3, [[2],[1,3],[1,2],[3]],  [[1,4],[1,2],[3,4],[2,3]])) # 2
print(obj.minimumTeachings(5, [[1],[5],[1,5],[5]],  [[1,2],[1,3],[1,4],[2,3]])) # 1



# Example 1:

# Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
# Output: 1
# Explanation: You can either teach user 1 the second language or user 2 the first language.
# Example 2:

# Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
# Output: 2
# Explanation: Teach the third language to users 1 and 3, yielding two users to teach.