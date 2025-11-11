from typing import List, Optional
from Utils import Node, ListNode


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
