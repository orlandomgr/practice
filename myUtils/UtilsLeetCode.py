from typing import List, Optional
from myUtils.Utils import ListNode

class UtilsLeetCode:
    def getListNodeFromArray(array: List[int]) -> Optional[ListNode]:
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
