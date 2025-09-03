const ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}
/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
    let value = 0;
    for (let i = 0; i < s.length; i++) {
        let str = s[i];
        if (['I', 'X', 'C'].includes(str)) {
            str += s[i + 1];
            if (i + 1 < s.length && ['IV', 'IX', 'XL', 'XC', 'CD', 'CM'].includes(str)) {
                i++;
            } else {
                str = s[i];
            }
        }
        value += ROMAN[str] || 0;
    }
    return value;
};

// console.log(romanToInt('MCMXCIV')); // 1994
// console.log(romanToInt('LVIII')); // 58
// console.log(romanToInt('IX')); // 9
// console.log(romanToInt('XLII')); // 42
// console.log(romanToInt('MMMCMXCIX')); // 1999
// console.log(romanToInt('MMMCMXC')); // 1990
console.log(romanToInt('DCXXI')); // 621