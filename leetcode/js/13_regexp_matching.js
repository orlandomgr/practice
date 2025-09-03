function expandMatches(matches, options) {
    let newMatches = [];
    // if (m.length === 0) {
    //     for (let o of options) {
    //         console.log("o: " + o)
    //         newMatches.push(m + o);
    //     }
    // } else {
        for (let m of matches) {
            // console.log("m: " + m)
            for (let o of options) {
                // console.log("o: " + o)
                newMatches.push(o + m);
            }
        }
    // }
    return newMatches;
}

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function (s, p) {
    let rules = [];
    for()
    // let eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
    if (p == ".*") {
        return true;
    }

    let matches = [""];
    let newStr = "";
    for (let i = p.length - 1; i >= 0; i--) {
        let c = p[i];
        let n = (i > 0) ? p[i - 1] : "";
        if (c == "*" && n == ".") {
            c = n + c;
        }
        let isSpecial = c == '.' || c == '*' || c == '.*';
        // console.log(isMatch("aab", "c*a*b")); // true


        if(isSpecial) {
            if(c == "."){
                s = s.substring(0, i) + s.substring(i + 1, s.length);
            }
        } else {
            newStr = c + newStr;

        }

        
        // if (c == '.*') {
        //     matches = expandMatches(matches, [n, n + n, ""]);
        //     i--;
        // } else if (c == '*') {
        //     matches = expandMatches(matches, [n, n + n, ""]);
        //     i--;
        // } else  if (c == '.') {
        //     matches = expandMatches(matches, eng);
        // } else {
        //     matches = expandMatches(matches, [c]);
        // }

        // console.log(newStr[i - 1] + " s " + s[i - 1]);
        // if (s[i] !== newStr[i - 1]) {
        //     newStr.slice(0, -1);
        // } else {
        //     newStr += c;
        // }
        // if (c == '.*') {
        //     newStr += s[i];
        //     newStr += s[i+1];
        //     i++;
        // } 
        //     // console.log(newStr);
        // } else if (c == '.'){
        //     newStr += s[i];
        // } else {
        //     newStr += c;
        // }
    }
    // console.log(s + " == " + newStr);
    // for (m of matches) {
    //     console.log(m);
    //     if (m === s) {
    //         return true;
    //     }
    // }
    // return false;
    console.log("s: " + s + " newStr: " + newStr);
    return newStr === s;
};

// console.log(isMatch("aa", "a")); // false
// console.log(isMatch("aa", "a*")); // true
// console.log(isMatch("ab", ".*")); // true
console.log(isMatch("abc", "a.c")); // true
// console.log(isMatch("abcdef", "abc.*f")); // true
// console.log(isMatch("aab", "c*a*b")); // true

// console.log(isMatch("ab", ".*c")); // false 
