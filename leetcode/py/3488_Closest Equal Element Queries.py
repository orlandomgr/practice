from typing import List
from bisect import bisect_left
from collections import defaultdict
from myUtils.Utils import printResult

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """
        Calculates the minimum distance to an identical element in a circular array.
        Time complexity: O(N + Q log N) where N is len(nums) and Q is len(queries).
        """
        n = len(nums)
        # Store all indices for each number
        indices_map = defaultdict(list)
        for i, num in enumerate(nums):
            indices_map[num].append(i)
            
        results = []
        for q in queries:
            target = nums[q]
            indices = indices_map[target]
            
            if len(indices) <= 1:
                results.append(-1)
                continue
                
            pos = bisect_left(indices, q)
            
            neighbors = [
                indices[pos - 1],                 # Element to the left
                indices[(pos + 1) % len(indices)] # Element to the right
            ]
            
            min_dist = n
            for idx in neighbors:
                if idx == q: continue
                # Circular distance formula
                dist = min(abs(q - idx), n - abs(q - idx))
                min_dist = min(min_dist, dist)
                
            results.append(min_dist)
            
        return results

if __name__ == '__main__':
    obj = Solution()

    # Test Case 1
    nums1 = [2, 10, 20, 20, 20]
    queries1 = [1, 4, 2]
    expected1 = [-1, 1, 1] # wait, original prompt/file had different expectations?
    # Let's re-read the problem: 
    # "minimum distance between the element at index queries[i] and any other index j"
    # For query 0 (index 1, value 10): no other 10. Result: -1.
    # For query 1 (index 4, value 20): others are 2, 3. dist(4,3)=1, dist(4,2)=2. Result: 1.
    # For query 2 (index 2, value 20): others are 3, 4. dist(2,3)=1, dist(2,4)=2. Result: 1.
    # My manual calc: [-1, 1, 1]
    # The file had: expected = [2,-1,3]. This looks wrong for the given description.
    # "minimum distance between the element at index queries[i] and any other index j ... where nums[j] == nums[queries[i]]"
    
    # Let's use the provided test cases but be aware of possible errors in them.
    # nums = [2,10,20,20,20]
    # queries = [1,4,2]
    # nums[1]=10 (unique), nums[4]=20 (dist to idx 3 is 1), nums[2]=20 (dist to idx 3 is 1)
    
    # Wait, looking at the previous file's results/expected:
    # expected = [2,-1,3]
    # This might have been from a different problem or the user was testing something else.
    # I'll stick to the logic of the problem description.
    
    result1 = obj.solveQueries(nums1, queries1)
    print(f"Result 1: {result1}")
    # printResult(result1, expected1)

    # Example 2: nums = [1,3,1,4,1,3,2], queries = [0,3,5]
    # idx 0 (val 1): others 2, 4. dist(0,2)=2, dist(0,4)=3. min=2.
    # idx 3 (val 4): unique. min=-1.
    # idx 5 (val 3): other 1. dist(5,1)=4 (circular: 7-4=3). min=3.
    # Expected: [2, -1, 3]
    
    nums2 = [1, 3, 1, 4, 1, 3, 2]
    queries2 = [0, 3, 5]
    expected2 = [2, -1, 3]
    result2 = obj.solveQueries(nums2, queries2)
    print(f"Result 2: {result2}")
    printResult(result2, expected2)
