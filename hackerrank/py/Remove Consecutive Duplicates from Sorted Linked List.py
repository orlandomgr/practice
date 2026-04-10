#!/bin/python3

import math
import os
import random
import re
import sys
from myUtils.Utils import printResult, SinglyLinkedListNode

#
# Complete the 'deleteDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteDuplicates(head):
    # Write your code here
    curr = head  
    prev = head
    while curr:
        prev = curr
        curr = curr.next
        while curr and prev.data == curr.data:
            curr = curr.next
        prev.next = curr

    return head

head = SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(2, SinglyLinkedListNode(2, SinglyLinkedListNode(3, SinglyLinkedListNode(4, SinglyLinkedListNode(4, SinglyLinkedListNode(5))))))))
expected = SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(3, SinglyLinkedListNode(4, SinglyLinkedListNode(5)))))
result = deleteDuplicates(head)
printResult(result, expected)

head = SinglyLinkedListNode(1)
expected = SinglyLinkedListNode(1)
result = deleteDuplicates(head)
printResult(result, expected)


