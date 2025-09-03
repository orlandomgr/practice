/**
 * @param {number} n
 * @param {number} m
 * @return {number}
 */
var flowerGame = function (n, m) {
    // if ((n + m) % 2 == 0) {
    //     return 0;
    // } else {
        return Math.floor((n * m) / 2);
    // }
};

console.log(flowerGame(3, 2)); // 3
console.log(flowerGame(1, 1)); // 3


// | | |
// | |

// A B A
// B A

// |
// |

// A
// B