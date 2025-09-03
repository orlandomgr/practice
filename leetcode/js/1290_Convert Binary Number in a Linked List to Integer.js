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
 * @return {number}
 */
var getDecimalValue = function (head) {
    if (!head) {
        return 0;
    }
    let result = "";
    let node = head;
    while (node) {
        result += node.val;
        node = node.next;
    }
    return parseInt(result, 2);
};

console.log(getDecimalValue(getNodes([1, 0, 1])));
console.log(getDecimalValue(getNodes([])));