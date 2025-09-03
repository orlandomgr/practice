const { Stack } = require('@datastructures-js/stack');

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

function isValidSwap(node, k) {
    let current = node;
    let result = true;
    for (let i = 1; i < k; i++) {
        if (!current || !current.next) {
            result = false;
            break;
        }
        current = current.next;
    }
    return result;
}

function swapNodes(node, k) {
    if (!isValidSwap(node, k)) {
        return null;
    };

    const stack = new Stack();
    let next;
    for (let i = 0; i < k; i++) {
        stack.push(node);
        node = node.next;
    }
    console.log(stack);
    next = node;
    node = stack.pop();
    let root = node;
    for (let i = 0; i < k; i++) {
        let newNode = stack.pop();
        node.next = newNode;
        if (i < k - 1) {
            node = node.next;
        }
    }
    node && (node.next = next);
    console.log("root");
    console.log(root);
    console.log("node");
    console.log(node);
    return { root, node };
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
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function (head, k) {
    let root = head;
    let current = head;
    let parent = null;
    while (current) {
        let nodes = swapNodes(current, k);
        if (nodes) {
            if (!parent) {
                root = nodes.root;
            } else {
                parent.next = nodes.root;
            }
            parent = nodes.node;
            current = parent.next;
        } else {
            break;
        }
    }
    return root;
};

console.log(reverseKGroup(getNodes([1, 2, 3, 4, 5]), 2)); // [2,1,4,3,5]
// console.log(reverseKGroup(getNodes([1, 2, 3, 4, 5]), 3)); // [3,2,1,4,5]
// console.log(reverseKGroup());

