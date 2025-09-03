/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function (s, numRows) {
    let result = "";
    let array = [[]];
    let idx = 0;
    let fwd = true;
    for(let i = 0; i < s.length; i++){
        let c = s[i];
        if(idx == numRows-1){
            fwd=false;
        }
        if(idx == 0){
            fwd = true;
        }
        if(!array[idx]){
            array[idx] = [];
        }
        array[idx].push(c);
        if(fwd){
            idx++;
        }else{
            idx--;
        }
    }
    for(let i in array){
        result += array[i].join('');
    }
    return result;
};

console.log(convert('PAYPALISHIRING', 3)); // PAHNAPLSIIGYIR
console.log(convert('PAYPALISHIRING', 4)); // PINALSIGYAHRPI

// Input: s = "PAYPALISHIRING", numRows = 3
// Output: "PAHNAPLSIIGYIR"


// Input: s = "PAYPALISHIRING", numRows = 4
// Output: "PINALSIGYAHRPI"
// Explanation:
// P     I    N
// A   L S  I G
// Y A   H R
// P     I
// Example 3:

// Input: s = "A", numRows = 1
// Output: "A"
