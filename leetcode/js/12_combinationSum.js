/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function (candidates, target) {
    // candidates.sort((a, b) => a - b);
    let nums = new Set(candidates);
    let combinations = [];
    for (let i = 0; i < candidates.length; i++) {
        let num = candidates[i];
        if (num == target) {
            combinations.push([num]);
            continue;
        }
        let sum = 0;
        let tmp = [];

        while (sum < target) {
            sum += num;
            tmp.push(num);
            if (sum == target) {
                break;
            }
        }
        if (sum != target) {
            while (sum > 0) {
                sum -= num;
                tmp.pop();
                let complement = target - sum;
                if (complement > num && nums.has(complement) && complement != target) {
                    tmp.push(complement);
                    sum += complement;
                    break;
                }
            }
        }
        if (sum == target) {
            combinations.push(tmp);
        }
    }
    return combinations;
};

function getArraySum(combination) {
    let sum = 0;
    for (i in combination) {
        sum += combination[i];
    }
    return sum;
}

function expandCombinations(combinations, candidates, target) {
    let success = [];
    let newCombinations = [];
    let limit = combinations.length;

    for (let i = 0; i < limit; i++) {
        let tmp = combinations[0];
        let sum = getArraySum(tmp);
        let last = tmp[tmp.length - 1];
        combinations.splice(0, 1);
        for (let j = 0; j < candidates.length; j++) {
            if (last > candidates[j]) {
                continue;
            }
            if (sum + candidates[j] == target) {
                success.push([...tmp, candidates[j]]);
            } else if (sum + candidates[j] < target) {
                newCombinations.push([...tmp, candidates[j]]);
            }
        }
    }
    return { success, newCombinations };
}

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function (candidates, target) {
    candidates = candidates.sort((a, b) => a - b);
    let result = [];
    let combinations = [];
    for (let i = 0; i < candidates.length; i++) {
        combinations.push([candidates[i]]);
        if(candidates[i] === target){
            result.push([candidates[i]])
        }
    }

    let tmp = expandCombinations(combinations, candidates, target);
    result.push(...tmp.success);
    while (tmp.newCombinations.length > 0) {
        tmp = expandCombinations(tmp.newCombinations, candidates, target);
        result.push(...tmp.success);
    }

    return result;
};

// console.log(combinationSum([2, 3], 8)); // [[2,2,2,2],[2,3,3],[3,5]]

console.log(combinationSum([2, 3, 6, 7], 7)); // [[2,2,3],[7]]
// console.log(combinationSum([2, 3, 5], 8)); // [[2,2,2,2],[2,3,3],[3,5]]
// console.log(combinationSum([2], 1)); // []
// console.log(combinationSum([1], 1)); // [[1]]
// console.log(combinationSum([1], 2)); // [[1,1]]
// console.log(combinationSum([2, 3], 5)); // [[2,3]]

