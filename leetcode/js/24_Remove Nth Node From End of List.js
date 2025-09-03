function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

function getNodes(values) {
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
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function (head, n) {
    let back = head;
    let curr = head;
    let idx = 0;
    for (let i = 0; i < n; i++) {
        curr = curr.next;
        if (!curr) {
            return head.next;
        }
    }
    while (curr.next) {
        back = back.next;
        curr = curr.next;
        idx++;
    }
    let tmp = back.next.next;
    back.next = tmp;
    return head;
};

console.log(removeNthFromEnd(getNodes([1]),1)); // []
console.log(removeNthFromEnd(getNodes([1, 2]), 1)); // [1]
console.log(removeNthFromEnd(getNodes([1, 2]), 2)); // [2]
console.log(removeNthFromEnd(getNodes([1, 2, 3]), 3)); // [2,3]
console.log(removeNthFromEnd(getNodes([1,2,3,4,5]),2)); // [1,2,3,5]
