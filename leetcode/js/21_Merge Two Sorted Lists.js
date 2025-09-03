function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

function getNodes(values) {
    if (values.length > 0) {
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
    return null;
}
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
    if (list1 == null && list2 == null) {
        return null;
    }
    let root = new ListNode(0, {});
    let current = root;
    while (list1 || list2) {
        let n1 = list1 && list1.val;
        let n2 = list2 && list2.val;
        if (n1 != null && n2 != null) {
            if (n1 < n2 || n2 == null) {
                current.next = new ListNode(n1, {});
                list1 = list1.next;
            } else {
                current.next = new ListNode(n2, {});
                list2 = list2.next;
            }
        } 
        else if (n1 != null) {
            current.next = new ListNode(n1, {});
            list1 = list1.next;
        } else {
            current.next = new ListNode(n2, {});
            list2 = list2.next;
        }
        current = current.next;
    }
    current.next = null;
    return root.next;
};


console.log(mergeTwoLists(getNodes([]), getNodes([]))); // []
console.log(mergeTwoLists(getNodes([1, 2, 4]), getNodes([1, 3, 4]))); // [1,1,2,3,4,4]
console.log(mergeTwoLists(getNodes([]), getNodes([0]))); // [0]
