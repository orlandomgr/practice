# Single Linked List 
# pointers head, element

# swap element with the one after 

# a -> b -> c
# b -> a -> c

# a -> c -> b

# LinkedList
# data
# next

def swapPointers(head: Node, element: Node) -> Node:
    if not head or not element:
        # raise("Invalid inputs")
        return head

    curr = head
    prev = curr
    visited = set()
    updated = False

    while curr:
        if curr in visited: 
            raise("Circular list")
        visited.add(curr)

        if curr == element:
            updated = True
            # swap
            future = element.next 
            if future:
                prev.next = future
                curr.next = future.next 
                future.next = curr

                if head == element:
                    head = future
            else:
                raise("Not possible to swap end")  
        prev = curr
        curr = curr.next
    
    if not updated:
        raise("Unable to swap elements. Element not found")

    return head


