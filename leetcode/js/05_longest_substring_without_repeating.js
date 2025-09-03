/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring2 = function(s) {
    let maxLength = 0;
    let knownChars = new Set();
    // for (let i = 0; i < s.length; i++) {
    //     if(knownChars.has(s[i])) {
    //         maxLength = Math.max(maxLength, knownChars.size);
    //         knownChars.clear();
    //     }
    //     knownChars.add(s[i]);
    // }
    // maxLength = Math.max(maxLength, knownChars.size);
    // // console.log(knownChars);
    // // console.log(maxLength);

    // knownChars.clear();
    for (let i = s.length - 1; i >= 0; i--) {
        if(knownChars.has(s[i])) {
            maxLength = Math.max(maxLength, knownChars.size);
            knownChars.clear();
        }
        knownChars.add(s[i]);
    }
    maxLength = Math.max(maxLength, knownChars.size);
    // console.log(knownChars);
    // console.log(maxLength);

    return maxLength;
};

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let maxLength = 0;
    let knownChars = new Set();
    let start = 0;
    for (let i = 0; i < s.length; i++) {
        if (knownChars.has(s[i])) {
            while (s[start] !== s[i]) {
                knownChars.delete(s[start]);
                start++;
            }
            start++;
        } else {
            knownChars.add(s[i]);
        }
        maxLength = Math.max(maxLength, i - start + 1);
    }

    return maxLength;
};


console.log(lengthOfLongestSubstring("abcabcbb")); // Output: 3
console.log(lengthOfLongestSubstring("bbbbb")); // Output: 1
console.log(lengthOfLongestSubstring("pwwkew")); // Output: 3
console.log(lengthOfLongestSubstring("")); // Output: 0
console.log(lengthOfLongestSubstring("a")); // Output: 1
console.log(lengthOfLongestSubstring(" ")); // Output:  1
console.log(lengthOfLongestSubstring("dvdf")); // Output:  3
console.log(lengthOfLongestSubstring("abcb")); // Output:  3
