function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

function getNodes(values) {
    if (values.length == 0) {
        return [];
    }
    let head = new ListNode(values[0], {});
    current = head;
    for (let i = 1; i < values.length; i++) {
        let leaf = new ListNode(values[i], {});
        current.next = leaf;
        current = leaf;
    }
    current.next = null;
    return head;
}

function swapNodes(node1, node2) {
    if (!node2) {
        return node1;
    }
    let tmp = node2.next;
    let tmpNode = node1;
    node1 = node2;
    node2 = tmpNode;
    node2.next = tmp;
    node1.next = node2;
    return node1;
}
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function (head) {
    let isHead = true;
    let root = head;
    let current = head;
    let swapped = head;
    while (current) {
        let tmp = swapNodes(current, current.next);
        if (isHead) {
            root = tmp;
            isHead = false;
        } else {
            swapped.next = tmp;
        }
        current = tmp;
        swapped = current.next;
        current = current.next && current.next.next;
    }
    return root;
};

// console.log(swapPairs(getNodes([1, 2, 3, 4]))); // [2,1,4,3]
// console.log(swapPairs(getNodes([1]))); // [1]
console.log(swapPairs(getNodes([1, 2, 3]))); // [2,1,3]
