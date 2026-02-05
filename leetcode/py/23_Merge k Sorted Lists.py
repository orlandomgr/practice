from myUtils.Utils import printResult
from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return f"ListNode: val='{self.val}', next={self.next}"
        # return f"{self.val, self.next}"
    def __repr__(self):
        return self.__str__()
    def __lt__(self, other):
        return self.val < other.val
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i in lists:
            # heapq.heappush(pq, i)
            # print(i)
            while i:
                heapq.heappush(pq, i.val)
                i = i.next
        
        # print(pq)
        # head = None
        if len(pq) > 0:
            head = ListNode(0, 0)
        else:
            head = ListNode()

        current = head
        while pq:
            tmp = heapq.heappop(pq)
            tmpNode = ListNode(tmp)
            current.next = tmpNode
            current = tmpNode

        return head.next    

obj = Solution()

l1 = ListNode(1)
l14 = ListNode(4)
l1.next = l14
l15 = ListNode(5)
l14.next = l15

l2 = ListNode(1)
l23 = ListNode(3)
l2.next = l23
l24 = ListNode(4)
l23.next = l24

l3 = ListNode(2)
l36 = ListNode(6)
l3.next = l36

lists = [l1,l2, l3]
expected = [1,1,2,3,4,4,5,6]
result = obj.mergeKLists(lists)
printResult(result, expected)

# lists = [ListNode()]
# expected = []
# result = obj.mergeKLists(lists)
# printResult(result, expected)

# lists = []
# expected = []
# result = obj.mergeKLists(lists)
# printResult(result, expected)
