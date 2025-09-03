/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function (s) {

    let nums = [];
    let isNegative = false;
    let isNChar = false;
    let isNumber = false;
    let result = 0;
    for (let i = 0; i < s.length; i++) {
        let c = s[i];
        if (c == " " && !isNumber) {
            continue;
        }
        if (c == "-" || c == "+") {
            if (!isNumber && !isNChar) {
                isNegative = (c == "-");
                isNChar = true;
                isNumber = true;
                continue;
            } else {
                break;
            }
        }

        if (["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"].includes(c)) {
            nums.push(c);
            isNumber = true;
        } else {
            break;
        }
    }
    if (nums.length > 0) {
        result += parseInt(nums[nums.length - 1]);
        for (let i = 0; i < nums.length - 1; i++) {
            result += nums[i] * Math.pow(10, nums.length - 1 - i);
            if (result > 2147483648) {
                break;
            }
        }
        if (isNegative) {
            result = result * -1;
        }
        if (result >= 2147483648) {
            return 2147483647;
        }
        if (result < -2147483648) {
            return -2147483648;
        }
    }
    return result;
};

console.log(myAtoi("123")); // 123
console.log(myAtoi("42")); // 42
console.log(myAtoi("-042")); // -42
console.log(myAtoi("1337c0d3")); // 1337
console.log(myAtoi("0-1")); // 0
console.log(myAtoi("words and 987")); // 0
console.log(myAtoi("-91283472332")); // -2147483648
console.log(myAtoi("  +  413")); // 0


