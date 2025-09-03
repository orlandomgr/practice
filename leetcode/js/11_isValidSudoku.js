function checkSquare(x, y, board) {
    let arrays = Array(10).fill(0);
    for (let i = x; i < x + 3; i++) {
        for (let j = y; j < y + 3; j++) {
            let value = board[j][i];
            if (value != '.') {
                if (arrays[value] >= 1) {
                    return false;
                } else {
                    arrays[value]++;
                }
            }
        }
    }
    return true;
}

function checkRow(board, row) {
    let arrays = Array(10).fill(0);
    for (let i = 0; i < board.length; i++) {
        let value = board[row][i];
        if (value != '.') {
            if (arrays[value] >= 1) {
                return false;
            } else {
                arrays[value]++;
            }
        }
    }
    return true;
}

function checkCol(board, col) {
    let arrays = Array(10).fill(0);
    for (let i = 0; i < board.length; i++) {
        let value = board[i][col];
        if (value != '.') {
            if (arrays[value] >= 1) {
                return false;
            } else {
                arrays[value]++;
            }
        }
    }
    return true;
}

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function (board) {

    let col = 1;
    var col3 = board.map(function(value, index) { return value[col]; });
    console.log(col3);

    for (let i = 0; i < board.length; i++) {
        if (!checkRow(board, i)) {
            return false;
        }
        if (!checkCol(board, i)) {
            return false;
        }
    }
    for (let i = 0; i < board.length; i += 3) {
        for (let j = 0; j < board[i].length; j += 3) {
            if (!checkSquare(i, j, board)) {
                return false;
            }
        }
    }
    return true;
};

console.log(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])); // true
console.log(isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]])); // false