function checkPalindrome(s, left, right){
    while (left >= 0 && right < s.length && s[left] === s[right]) {
        left--;
        right++;
    }
    return right - left - 1; 
}

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    if (s.length < 2) return s;

    let start = 0, end = 0;
    for (let i = 0; i < s.length; i++) {
        let len1 = checkPalindrome(s, i, i);
        let len2 = checkPalindrome(s, i, i + 1);
        let len = Math.max(len1, len2);

        if (len > end - start) {
            start = i - Math.floor((len - 1) / 2);
            end = i + Math.floor(len / 2);
        }
    }

    return s.substring(start, end + 1);
    
};

console.log(longestPalindrome("babad")); // Output: "bab" or "aba"
console.log(longestPalindrome("cbbd")); // Output: "bb"
console.log(longestPalindrome("a")); // Output: "a"
console.log(longestPalindrome("ac")); // Output: "a" or "c"
console.log(longestPalindrome("aba")); // Output: "a" or "c"
console.log(longestPalindrome("xabax")); // Output: "a" or "c"
console.log(longestPalindrome("xabay")); // Output: "a" or "c"
