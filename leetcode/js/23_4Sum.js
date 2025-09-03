/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function (nums, target) {
    nums = nums.sort((a, b) => a - b);
    let result = [];
    if (nums.length < 4) {
        return [];
    } else {
        let l = 0;
        let r = 0;
        let sum = 0;
        for (let i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            for (let j = i + 1; j < nums.length; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    continue;
                }
                l = j + 1;
                r = nums.length - 1;
                sum = 0;
                while (i < j && j < l && l < r && l < nums.length) {
                    if (l - 1 > j && nums[l] == nums[l - 1]) {
                        l++;
                        continue;
                    } else if (nums[r] == nums[r + 1]) {
                        r--;
                        continue;
                    }
                    sum = nums[i] + nums[j] + nums[l] + nums[r];
                    if (sum == target && i != j && j != l && l != r) {  //  && i < j && j < l && l < r
                        result.push([nums[i], nums[j], nums[l], nums[r]]);
                        if (nums[r] > nums[l]) {
                            r--;
                        } else {
                            l++;
                        }
                    } else {
                        if (sum < target) {
                            l++;
                        } else {
                            r--;
                        }
                    }
                }
            }
        }
    }
    return result;
};

// console.log("sum: " + sum + " i: " + nums[i] + " j: " + nums[j] + " l: " + nums[l] + " r: " + nums[r]);

console.log(fourSum([1, 0, -1, 0, -2, 2], 0)); // [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
console.log(fourSum([2, 2, 2, 2], 8)); // [2,2,2,2]
console.log(fourSum([0], 0)); // []

console.log(fourSum([-2, -1, -1, 1, 1, 2, 2], 0)); // [[-2,-1,1,2],[-1,-1,1,1]]

-2, -1, -1, 1, 1, 2, 2
