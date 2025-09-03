// const { Stack } = require('@datastructures-js/stack');

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

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
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

function getMiddleNode(head) {
    if (!head) {
        return head;
    }
    let prev = null;
    let n1 = head;
    let n2 = head.next;
    while (n2 && n2.next != null) {
        prev = n1;
        n1 = n1.next;
        n2 = n2.next && n2.next.next;
    }
    if (!prev) {
        prev = n1;
        n1 = n2;
    }
    return { n1, prev };
}

function bst(head) {
    if (head && !head.next) {
        return new TreeNode(head.val, null, null);
    }
    let middle = getMiddleNode(head);
    if (middle && middle.n1.val != head.val) {
        middle.prev && (middle.prev.next = null);
        return new TreeNode(middle.n1.val, bst(head), bst(middle.n1.next));
    }
}

/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function (head) {
    if (!head || head.length == 0) {
        return null;
    }
    return bst(head);
};

console.log(sortedListToBST(getNodes([-10, -3, 0, 5, 9]))); // [0,-3,9,-10,null,5] or [0,-3,9,-10,null,5]
console.log(sortedListToBST(getNodes([]))); // []
console.log(sortedListToBST(getNodes([0])));