function getFactorialArray(n) {
    if (n < 0) {
        return -1;
    }
    let array = new Array(n).fill(1);
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
        array[i] = result;
    }
    return array;
}

function getMirrored(str, n) {
    let mirrored;
    if (n % 2 == 0) {
        mirrored = str + str.split('').reverse().join('');
    } else {
        let s = str.substring(0, str.length - 1);
        mirrored = s + str.charAt(str.length - 1) + s.split('').reverse().join('');
    }
    return mirrored;
};

function getPermutations(n, data) {
    let total = 0;
    let factArray = getFactorialArray(n + 1);
    for (let item of data) {
        let numbers = new Array(10).fill(0);
        for (let c of item) {
            numbers[parseInt(c)]++;
        }
        let permutations = 0;
        let p = 0;
        for (let i = 1; i < numbers.length; i++) {
            if (numbers[i] == 0) {
                continue;
            }
            numbers[i]--;
            p = factArray[n - 1];
            for (let c of numbers) {
                p = Math.floor(p / factArray[c]);
            }
            permutations += p;
            numbers[i]++;
        }
        total += permutations;
    }
    return total;
}

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var countGoodIntegers = function (n, k) {
    let middle = Math.floor((n + 1) / 2);
    let start = Math.pow(10, middle - 1);
    let end = Math.pow(10, middle) - 1;
    let data = new Set();
    for (let i = start; i <= end; i++) {
        let str = i.toString();
        let mirrorStr = getMirrored(str, n);
        if(!mirrorStr){
            continue;
        }
        let mirror = parseInt(mirrorStr);
        if (mirror % k == 0) {
            data.add(mirrorStr.split('').sort().join(''));
        }
    }
    data = Array.from(data);
    return getPermutations(n, data);
};


console.log(countGoodIntegers(4, 1)); // 252
console.log(countGoodIntegers(1, 1)); // 9
console.log(countGoodIntegers(3, 5)); // 27
console.log(countGoodIntegers(1, 4)); // 2
console.log(countGoodIntegers(5, 6)); // 2468

