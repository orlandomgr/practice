/**
 * @param {number} n
 * @param {number} k
 * @param {number} maxPts
 * @return {number}
 */
var new21Game = function (n, k, maxPts) {
    if (k === 0 || n >= k + maxPts - 1) {
        return 1.0;
    }
    let dp = new Array(n + 1).fill(0);
    dp[0] = 1.0;

    let windowSum = dp[0];
    let result = 0;
    for (let i = 1; i <= n; i++) {
        dp[i] = windowSum / maxPts;

        if (i < k) {
            windowSum += dp[i];
        } else {
            result += dp[i];
        }
        if (i - maxPts >= 0) {
            windowSum -= dp[i - maxPts];
        }
    }

    return result;
};

console.log(new21Game(10, 1, 10)); // Example test case
console.log(new21Game(6, 1, 10)); // Example test case
console.log(new21Game(21, 17, 10)); // Example test case
console.log(new21Game(0, 0, 1)); // Edge case
console.log(new21Game(100, 50, 10)); // Example test case
console.log(new21Game(10, 10, 10)); // Example test case
console.log(new21Game(1, 1, 1)); // Edge case