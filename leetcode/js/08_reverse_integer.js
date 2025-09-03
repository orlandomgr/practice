/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    if(x >= 0 && x < 10){
        return x;
    }

    let newNumber = 0;
    let isNegative = x < 0;
    x = Math.abs(x);
    let numbers = [];
    while(x > 0){
        let lastDigit = x % 10;
        x = Math.floor(x / 10);
        numbers.push(lastDigit);
    }
    for(let i = 0; i < numbers.length; i++) {
        newNumber += numbers[i] * Math.pow(10, numbers.length - i - 1);
    }
    if(isNegative) {
        newNumber = -newNumber;
    }
    if(newNumber < -Math.pow(2, 31) || newNumber > Math.pow(2, 31) - 1) {
        return 0;
    }
    return newNumber;
};

console.log(reverse(123)); // Output: 321
console.log(reverse(-123)); // Output: -321
console.log(reverse(120)); // Output: 21    
