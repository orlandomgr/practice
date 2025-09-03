from typing import List, Optional

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

    def __str__(self):
        return f"ListNode: val='{self.val}', next={self.next}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode: val='{self.val}', left={self.left}, right={self.right}"

class HackerUtils:
    def getNodeFromArray(self, array: List[int]) -> Optional[Node]:
        if len(array) == 0:
            return None

        head = Node(array[0], {})
        current = head
        for item in array:
            print(item)
            leaf = ListNode(item, {})
            current.next = leaf
            current = leaf
        current.next = None
        return head


class LeetUtils:
    def getListNodeFromArray(self, array: List[int]) -> Optional[ListNode]:
        if len(array) == 0:
            return None

        head = ListNode(array[0], {})
        current = head
        for item in array:
            print(item)
            leaf = ListNode(item, {})
            current.next = leaf
            current = leaf
        current.next = None
        return head
 