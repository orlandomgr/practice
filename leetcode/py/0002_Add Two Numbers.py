from typing import Optional
from utils.FugaUtils import ListNode, LeetUtils


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        aux = 0
        current = root
        while l1 or l2 or aux > 0:
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + aux

            current.val = value % 10
            aux = value // 10

            if((not l1 or not l1.next) and (not l2 or not l2.next) and aux == 0):
                break
            
            current.next = ListNode(0)

            l1 = l1 and l1.next
            l2 = l2 and l2.next
            current = current.next

        return root

obj = Solution()
array1 = LeetUtils().getListNodeFromArray([2,4,3])
array2 = LeetUtils().getListNodeFromArray([5,6,4])
result = obj.addTwoNumbers(array1, array2)
print(result)

array1 = LeetUtils().getListNodeFromArray([])
array2 = LeetUtils().getListNodeFromArray([])
result = obj.addTwoNumbers(array1, array2)
print(result)

array1 = LeetUtils().getListNodeFromArray([9,9,9,9,9,9,9])
array2 = LeetUtils().getListNodeFromArray([9,9,9,9])
result = obj.addTwoNumbers(array1, array2)
print(result)