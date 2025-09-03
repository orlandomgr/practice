function addSingles(s) {
    s += "()";
    return s;
}

function addEmbeeded(s) {
    s = "(" + s + ")";
    return s;
}

function combine(arr1, arr2) {
    let result = new Set();
    for (let item1 of arr1) {
        for (let item2 of arr2) {
            result.add(item1 + item2);
            result.add(item2 + item1);
        }
    }
    return result;
}

function getCombinationPairs(n) {
    let result = [];
    if (n > 2) {
        result.push([1, n - 1]);
        for (let i = n - 2; i > n; i--) {
            result.push([i, n - i]);
        }
    }
    return result;
}

/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
    let calc = new Map();
    let one = new Set();
    one.add("()");
    calc.set(1, one);
    if (n == 1) {
        return Array.from(calc.get(n));
    }
    for (let i = 2; i <= n; i++) {
        let options = new Set();
        let prev = calc.get(i - 1);
        for (let s of prev) {
            options.add(addSingles(s));
            options.add(addEmbeeded(s));
        }

        let pairs = getCombinationPairs(i);
        console.log(pairs);
        for (let item of pairs) {
            let arr1 = calc.get(item[0]) || [];
            let arr2 = calc.get(item[1]) || [];
            let comb = combine(arr1, arr2);
            comb.forEach(item => options.add(item));
        }
        calc.set(i, options);
    }
    return Array.from(calc.get(n));
};

// console.log(generateParenthesis(1)); // ["()"] 1
// console.log(generateParenthesis(2)); // ["(())", "()()"] 2
// console.log(generateParenthesis(3)); // ["((()))","()()()","(()())","(())()","()(())"] 3  
// console.log(generateParenthesis(4)); // ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"] 4
console.log(generateParenthesis(6)); 


