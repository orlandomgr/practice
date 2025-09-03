const LETTERS = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

function getCombinations(arr1, arr2) {
    let result = [];
    for (let item1 of arr1) {
        let item = item1;
        for (let item2 of arr2) {
            result.push(item + item2);
        }
    }
    return result;
}
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
    let result = [];
    if (digits.length > 0) {
        if (digits.length == 1) {
            return LETTERS[digits[0]];
        }
        result = LETTERS[digits[0]];
        for (let i = 1; i < digits.length; i++) {
            result = getCombinations(result, LETTERS[digits[i]]);
        }
    }
    return result;
};

console.log(letterCombinations("23")); // ["ad","ae","af","bd","be","bf","cd","ce","cf"]
console.log(letterCombinations("")); // []
console.log(letterCombinations("2")); // ["a","b","c"]
console.log(letterCombinations("234")); // ["adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi", "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi", "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"]
