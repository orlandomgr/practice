/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if(x < 0) return false;
    if(x < 10) return true;
    let str = x.toString();
    for(let i = 0; i < str.length/2; i++) {
        if(str[i] !== str[str.length - 1 - i]) {
            return false; 
        }
    }
    return true; 

    // let arr=[];
    // while (x > 0) {
    //     arr.push(x % 10);
    //     x = Math.floor(x / 10);
    // }
    // for (let i = 0; i < arr.length / 2; i++) {
    //     if (arr[i] !== arr[arr.length - 1 - i]) {
    //         return false;
    //     }
    // }
    // return true;

};

// console.log(isPalindrome(121)); // true
// console.log(isPalindrome(-121)); // false
// console.log(isPalindrome(10)); // false
console.log(isPalindrome(12321)); // true
// console.log(isPalindrome(0)); // true
// console.log(isPalindrome(1234321)); // true
// console.log(isPalindrome(123456789987654321)); // true
// console.log(isPalindrome(12345678987654321)); // true
// console.log(isPalindrome(1234567890)); // false
// console.log(isPalindrome(1234567890123456789)); // true
// console.log(isPalindrome(1234567890987654321)); // true