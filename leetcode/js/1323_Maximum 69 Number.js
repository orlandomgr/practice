/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number  = function(num) {
    let nums = [];
    while(num > 0){
        let dec = num % 10;
        nums.push(dec);
        num = Math.floor(num / 10);
    }
    let toBeChanged = true;
    let result = 0;
    for(let i = nums.length-1; i >= 0; i--){
        let x = nums[i];
        if(toBeChanged && x != 9){
            x = 9;
            toBeChanged = false;
        }
        result += x * Math.pow(10, i);
    }
    return result;
};

console.log(maximum69Number(9669)); // 9969
console.log(maximum69Number(9996)); // 9999
console.log(maximum69Number(9999)); // 9999
// console.log(maximum69Number());
