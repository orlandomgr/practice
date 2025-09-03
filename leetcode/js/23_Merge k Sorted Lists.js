const {
    PriorityQueue,
} = require('@datastructures-js/priority-queue');

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

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
    let pq = new PriorityQueue((a, b) => {
        if (!a) {
            return 1;
        }
        if (!b) {
            return -1;
        }
        return a.val - b.val;
    });
    for (let i = 0; i < lists.length; i++) {
        pq.push(lists[i]);
    }
    let head;
    if (pq.size() > 0) {
        head = new ListNode(0, {});
    } else {
        head = new ListNode();
    }
    current = head;
    while (current) {
        let tmp = pq.dequeue();
        current.next = tmp;
        current = tmp;
        if (current && current.next) {
            pq.push(current.next);
        }
    }
    return head.next;
};

// console.log(mergeKLists([getNodes([1, 4, 5]), getNodes([1, 3, 4]), getNodes([2, 6])])); // [1,1,2,3,4,4,5,6]
// console.log(mergeKLists([getNodes([1, 4, 5]), getNodes([1, 3, 4]), getNodes([2, 6])])); // [1,1,2,3,4,4,5,6]
console.log(mergeKLists([getNodes([])])); // []
// console.log(mergeKLists([getNodes([]), getNodes([])])); // []
// console.log(mergeKLists([getNodes([]), getNodes([1])])); // [1]

