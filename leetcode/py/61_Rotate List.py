from myUtils.Utils import printResult, ListNode
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def toArray(self, head: Optional[ListNode]):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return head
        
        lastNode = head
        n = 1
        while lastNode.next:
            n += 1
            lastNode = lastNode.next

        # print(n)
        k = k % n
        lastNode.next = head

        curr = head
        for _ in range(n - k - 1):
            curr = curr.next

        result = curr.next
        curr.next = None

        return result

obj = Solution()

n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
head = ListNode(1, n2)
k = 2
headE = ListNode(4)
headE.next = ListNode(5)
headE.next.next = ListNode(1)
headE.next.next.next = ListNode(2)
headE.next.next.next.next = ListNode(3)
expected = headE
result = obj.rotateRight(head, k)
printResult(obj.toArray(result), obj.toArray(expected))

