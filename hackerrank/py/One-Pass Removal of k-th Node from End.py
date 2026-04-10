#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult, SinglyLinkedListNode

#
# Complete the 'removeKthNodeFromEnd' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def removeKthNodeFromEnd(head, k):
    k_node = head
    temp = head
    count = 0
    
    while temp.next:
        if count > k:
            k_node = k_node.next
        temp = temp.next
        count += 1
    
    if k_node == head and count == k:
        head = head.next
    elif count > k: 
        k_node.next = k_node.next.next
    return head

def removeKthNodeFromEnd2(head, k):
    if k < 0:
        return head

    dummy = SinglyLinkedListNode(0, head)
    fast = dummy
    slow = dummy
    
    for _ in range(k + 1):
        if not fast.next:
            return head
        fast = fast.next
        
    while fast.next:
        fast = fast.next
        slow = slow.next

    if slow.next:
        slow.next = slow.next.next
    return dummy.next


head = SinglyLinkedListNode(5, SinglyLinkedListNode(6, SinglyLinkedListNode(7, SinglyLinkedListNode(8))))
# [5, 6, 7, 8]
k = 3
expected = SinglyLinkedListNode(6, SinglyLinkedListNode(7, SinglyLinkedListNode(8)))
result = removeKthNodeFromEnd2(head, k)
printResult(result, expected)

head = SinglyLinkedListNode(5)
k = 1
expected = SinglyLinkedListNode(5)
result = removeKthNodeFromEnd2(head, k)
printResult(result, expected)

head = SinglyLinkedListNode(1, SinglyLinkedListNode(2))
k = 0
expected = SinglyLinkedListNode(1)
result = removeKthNodeFromEnd2(head, k)
printResult(result, expected)

