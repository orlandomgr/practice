/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

function getListNode(value) {
    let root = new ListNode(0);
    if (value === 0) {
        return root;
    }
    let current = root;
    while (value > 0) {
        current.next = new ListNode(value % 10);
        value = Math.floor(value / 10);
        current = current.next;
    }
    return root.next;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
    let root = new ListNode(0);
    let aux = 0;
    let current = root;
    while (l1 || l2 || aux > 0) {
        let value = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + aux;

        current.val = value % 10;
        aux = Math.floor(value / 10);

        if((!l1 || !l1.next) && (!l2 || !l2.next) && aux === 0) {
            break;
        }
        current.next = new ListNode(0);

        l1 = l1 && l1.next;
        l2 = l2 && l2.next;
        current = current.next;
    }
    return root;
};

console.log(addTwoNumbers(getListNode(342), getListNode(465))); // Output: ListNode representing 807
// console.log(addTwoNumbers(getListNode(9999999), getListNode(9999))); // Output: ListNode representing 807
// 9, 9, 9, 9, 9, 9, 9
// 9, 9, 9, 9
// console.log(addTwoNumbers(getListNode(0), getListNode(0))); // Output: ListNode representing 0
console.log(addTwoNumbers(getListNode(9), getListNode(1))); // Output: ListNode representing 10
// console.log(addTwoNumbers(getListNode(999), getListNode(1))); // Output: ListNode representing 1000


