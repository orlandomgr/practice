function division(dividend, divisor) {
    let count = 1;
    while (divisor < dividend) {
        let tmp = divisor << 1;
        if (tmp >= 1073741824 || dividend < tmp || tmp < 0) {
            break;
        }
        divisor = tmp;
        count = count + count;
    }
    let remaining = dividend - divisor;
    return { remaining, divisor, count };
}

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function (dividend, divisor) {
    if (dividend == 0) {
        return 0;
    }
    let maxNumber = 2147483647;
    let minNumber = -2147483648;
    let result = 0;
    let sign = (dividend < 0 ^ divisor < 0) ? -1 : 1;;
    dividend = Math.abs(dividend);
    divisor = Math.abs(divisor);
    if (divisor == 1) {
        result = dividend;
    } else if (divisor == dividend) {
        result = 1;
    } else {
        let count = 0;
        while (dividend > 0 && dividend >= divisor) {
            let res = division(dividend, divisor);
            count += res.count;
            dividend = res.remaining;
            result += res.count;
        }
    }
    result *= sign;
    if (result > maxNumber) {
        return maxNumber;
    }
    if (result < minNumber) {
        return minNumber;
    }
    return result;
};


console.log(divide(1100540749, -1090366779)); // 1073741823

// console.log(divide(2147483647, 2)); // 1073741823
// console.log(divide(2, 2)); // 1
// console.log(divide(1, 2)); // 0
// console.log(divide(10, 3)); // 3
// console.log(divide(30, 3)); // 3
// console.log(divide(7, -3)); // -2
// console.log(divide(-2147483648, -1)); // 2147483647
// console.log(divide(2147483647, 1)); // 2147483647
// console.log(divide(2147483647, -1)); // -2147483647
// console.log(divide(-2147483648, 4)); // -536870912  -536870913 

