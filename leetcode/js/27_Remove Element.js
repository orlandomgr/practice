/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
    let newSize = 0;
    let end = nums.length - 1;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] == val) {
            nums[i] = nums[end];
            nums[end] = "_";
            end--;
            i--;
            newSize--;
        } else {
            newSize++;
        }
    }
    return newSize;
};

console.log(removeElement([3, 2, 2, 3], 3)); // 2
console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)); // 5
// console.log(removeElement());
// console.log(removeElement());
