/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function (secret, guess) {
    let k = new Map();
    let A = 0;
    let B = 0;

    for (let i = 0; i < secret.length; i++) {
        if (secret[i] == guess[i]) {
            A++;
        } 
        // else {
            if (!k.has(secret[i])) {
                k.set(secret[i], 1);
            } else {
                let val = k.get(secret[i]);
                val++;
                k.set(secret[i], val);
            }
        // }
    }
    for (let i = 0; i < secret.length; i++) {
        let key = guess[i];
        if (k.has(key)) {
            let val = k.get(key);
            if (val > 0) {
                B++;
                val--;
                k.set(key, val);
            }
        }
    }
    return `${A}A${B - A}B`;
};

console.log(getHint("1807", "7810")); // "1A3B"
console.log(getHint("1123", "0111")); // "1A1B"
console.log(getHint("11", "10")); // "1A0B"

