/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum2 = function (nums, k) {
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        // console.log("i: " + nums[i]);
        if (nums[i] == k) {
            count++;
            // continue;
        }
        let sum = nums[i];
        for (let j = i + 1; j < nums.length; j++) {
            // console.log("j: " + nums[j]);
            sum += nums[j];
            // console.log("sum: " + sum);
            if (k == sum) {
                count++;
            }
        }
    }
    return count;
};

var subarraySum = function (nums, k) {
    let count = 0;
    let map = { 0: 1 };
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        sum += nums[i];
        let remaining = sum - k;
        if (map[remaining]) {
            count += map[remaining];
        }
        if (!map[sum]) {
            map[sum] = 0;
        }
        map[sum] += 1;
    }

    return count;
};

console.log(subarraySum([1, 1, 1], 2)); // 2
console.log(subarraySum([1, 2, 3], 3)); // 2
console.log(subarraySum([1, -1, 0], 0)); // 3
console.log(subarraySum([0, 0], 0)); // 3

console.log(subarraySum([28, 54, 7, -70, 22, 65, -6], 100)); // 1

