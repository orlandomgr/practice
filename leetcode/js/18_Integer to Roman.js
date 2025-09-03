const ROMAN = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

function getRomanLetter(num) {
    let n = num;
    let str = '';
    while (n > 0) {
        // console.log(n);
        if (ROMAN[n]) {
            let times = Math.floor(num / n);
            // console.log("times: " + times);
            for (let x = 0; x < times; x++) {
                str += ROMAN[n];
                // console.log("times: " + times + " str: " + str + " ROMAN[n]: " + ROMAN[n] + " n: " + n);
            }
            n = num - (n * times);
            num = n;
        } else {
            // console.log(" n: " + n);
            n--;
        }
    }
    return str;
}

/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
    let str = "";
    let nums = [];
    while (num > 0) {
        let dec = num % 10;
        num = Math.floor(num / 10);
        nums.unshift(dec);
    }

    for (let i = nums.length - 1; i >= 0; i--) {
        let num = nums[i] * Math.pow(10, nums.length - 1 - i);
        str = getRomanLetter(num) + str;
    }

    return str;
};

// console.log(intToRoman(3749)); // MMMDCCXLIX
// console.log(intToRoman(58)); // LVIII
// console.log(intToRoman(1994)); // MCMXCIV
console.log(intToRoman(2443)); // MMCDXLIII