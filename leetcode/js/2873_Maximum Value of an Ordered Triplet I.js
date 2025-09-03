/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumTripletValue = function (nums) {
    let max = 0;
    for (let i = 0; i < nums.length - 2; i++) {
        for (let j = i + 1; j < nums.length - 1; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                let value = (nums[i] - nums[j]) * nums[k];
                max = Math.max(max, value);
            }
        }
    }
    return max;
};

console.log(maximumTripletValue([12,6,1,2,7])); // 77
console.log(maximumTripletValue([1,10,3,4,19])); // 133
console.log(maximumTripletValue([1,2,3])); // 0
