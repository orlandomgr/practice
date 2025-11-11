from typing import List
from collections import defaultdict

def printResult(result, expected):
        if result == expected:
            print("\033[92mStatus: %s result: %s expected: %s\033[0m" % (result == expected, result, expected))
        else:
            print("\033[91mStatus: %s result: %s expected: %s\033[0m" % (result == expected, result, expected))

def getFreq(nums: List[int]):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 0
        freq[num] += 1
    return freq      

class Node:
    def __init__(self, info=0, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node: info='{self.info}', left={self.left}, right={self.right}"

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def setNext(self, next):
        self.next = next

    def __str__(self):
        return f"ListNode: val='{self.val}', next={self.next}"
    
    def __repr__(self):
        return self.__str__()

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode: val='{self.val}', left={self.left}, right={self.right}"
