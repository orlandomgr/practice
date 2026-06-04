from typing import List
from myUtils.Utils import printResult

"""
You are given an integer mass, which represents the original mass of a planet. You are further given an integer array asteroids, where asteroids[i] is the mass of the ith asteroid.

You can arrange for the planet to collide with the asteroids in any arbitrary order. If the mass of the planet is greater than or equal to the mass of the asteroid, the asteroid is destroyed and the planet gains the mass of the asteroid. Otherwise, the planet is destroyed.

Return true if all asteroids can be destroyed. Otherwise, return false.
"""

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # Destroy smaller asteroids first so the planet grows as much as possible.
        asteroids.sort()
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid
        return True


obj = Solution()

mass = 10
asteroids = [3,9,19,5,21]
expected = True
result = obj.asteroidsDestroyed(mass, asteroids)
printResult(result, expected)

mass = 5
asteroids = [4,9,23,4]
expected = False
result = obj.asteroidsDestroyed(mass, asteroids)
printResult(result, expected)

