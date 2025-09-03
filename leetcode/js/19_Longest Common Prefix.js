/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix2 = function (strs) {
    let pArray = [];
    for (let i = 0; i < strs[0].length; i++) {
        let c = strs[0][i];
        let same = true;
        for (let j = 1; j < strs.length; j++) {
            if (i >= strs[j].length || strs[j][i] != c) {
                same = false;
                break;
            }
        }
        if (same) {
            pArray.push(c);
        } else {
            break;
        }
    }
    return pArray.join("");
};

var longestCommonPrefix = function (strs) {
    let prefix = "";
    for (let i = 0; i < strs[0].length; i++) {
        let c = strs[0][i];
        let same = true;
        for (let j = 1; j < strs.length; j++) {
            if (i >= strs[j].length || strs[j][i] != c) {
                same = false;
                break;
            }
        }
        if (same) {
            prefix += c;
        } else {
            break;
        }
    }
    return prefix;
};

console.log(longestCommonPrefix(["flower", "flow", "flight"])); // fl
console.log(longestCommonPrefix(["dog", "racecar", "car"])); // ""
// console.log(longestCommonPrefix());
