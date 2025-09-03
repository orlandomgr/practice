var twoSum = function (nums, target) {
    let prev = new Map();
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i]
        let diff = target - num;
        if (prev.has(diff)) {
            return [prev.get(diff), i];
        } else {
            prev.set(num, i);
        }
    }
};

console.log(twoSum([2, 7, 11, 15], 9)); // Example usage [0, 1]
console.log(twoSum([1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 7, 1, 1, 1, 1, 1], 11)); // [5,11]