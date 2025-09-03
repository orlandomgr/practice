
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest2 = function (nums, target) {
    nums = nums.sort((a, b) => a - b);
    let min = Number.MAX_VALUE;
    let l_sum = 0;
    let result = 0;
    for (let i = 0; i < nums.length - 2; i++) {
        l_sum = nums[i] + nums[i + 1] + nums[i + 2];
        let subs = Math.abs(target - l_sum);
        console.log("l_sum: " + l_sum + " i: " + nums[i] + " 1: " + nums[i + 1] + " 2: " + nums[i + 2] + " subs: " + subs);
        if (subs < min) {
            min = subs;
            result = l_sum;
        }
        // min = Math.min(min, subs);
    }
    return result;
};

var threeSumClosest = function (nums, target) {
    nums = nums.sort((a, b) => a - b);
    let result = 0;
    if (nums.length < 3) {
        return 0;
    } else {
        let l = 0;
        let r = 0;
        let sum = 0;
        let min = Number.MAX_SAFE_INTEGER;
        for (let i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            l = i + 1;
            r = nums.length - 1;
            sum = 0;
            while (i < r && l < nums.length) {
                // if (l - 1 > i && nums[l] == nums[l - 1]) {
                //     l++;
                //     continue;
                // } else if (nums[r] == nums[r + 1]) {
                //     r--;
                //     continue;
                // }
                sum = nums[i] + nums[l] + nums[r];
                let diff = Math.abs(target - sum);
// console.log("sum: " + sum + " diff: " + diff + " i: " + nums[i] + " l: " + nums[l] + " r: " + nums[r]);
                if (diff < min && i != l && l != r) {
                    min = diff;
                    result = sum;
                    if(nums[r] >= nums[l]){
                        r--;
                    }else{
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
    return result;
};

                // console.log("sum: " + sum + " diff: " + diff + " i: " + nums[i] + " l: " + nums[l] + " r: " + nums[r]);

console.log(threeSumClosest([10,20,30,40,50,60,70,80,90], 1)); // 60
console.log(threeSumClosest([1, 1, 1, 0], -100)); // 2
console.log(threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], -2)); // -2
console.log(threeSumClosest([0, 0, 0], 1)); // 0
console.log(threeSumClosest([-1, 2, 1, -4], 1)); // 2
console.log(threeSumClosest([2, 5, 6, 7], 16)); // 15
console.log(threeSumClosest([-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1], -8)); // -7
// console.log(threeSumClosest());

