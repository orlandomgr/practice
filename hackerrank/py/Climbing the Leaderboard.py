#!/bin/python3

import sys
from myUtils.Utils import printResult

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    """
    Computes the rank of each player score against a leaderboard.
    The leaderboard is updated with each player score, but since player scores
    are non-decreasing, we can find the rank efficiently in O(N + M) time.
    """
    scores = sorted(set(ranked), reverse=True)
    
    results = []
    i = len(scores) - 1
    
    for p in player:
        while i >= 0 and p >= scores[i]:
            i -= 1
        results.append(i + 2)
        
    return results

if __name__ == '__main__':
    # Test Case 1
    ranked1 = [100, 90, 90, 80]
    player1 = [70, 80, 105]
    expected1 = [4, 3, 1]
    result1 = climbingLeaderboard(ranked1, player1)
    print(f"Test 1 - Result: {result1}")
    printResult(result1, expected1)

    # Test Case 2
    ranked2 = [100, 100, 50, 40, 40, 20, 10]
    player2 = [5, 25, 50, 120]
    expected2 = [6, 4, 2, 1]
    result2 = climbingLeaderboard(ranked2, player2)
    print(f"Test 2 - Result: {result2}")
    printResult(result2, expected2)
