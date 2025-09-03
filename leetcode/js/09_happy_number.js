function calculate2(n) {
    let str = n.toString();
    let total = 0;
    for (let i in str) {
        let digit = parseInt(str[i]);
        total += digit * digit;
    }
    return total;
}

function calculate(n) {
    let total = 0;
    while(n > 0){
        let lastDigit = n % 10;
        n = Math.floor(n / 10);
        total += lastDigit * lastDigit;
    }
    return total;
}
/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
    let calculated = [];
    while (n != 1) {
        if (calculated.includes(n)) {
            return false;
        }

        calculated.push(n);
        n = calculate(n);
    }
    return true;
};

console.log(isHappy(19)); // Output: true
console.log(isHappy(2)); // Output: false
console.log(isHappy(7)); // Output: true
console.log(isHappy(1)); // Output: true
