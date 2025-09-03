function checkSquare(board, row, col, num) {
    let x = Math.floor(row / 3) * 3;
    let y = Math.floor(col / 3) * 3;
    for (let i = x; i < x + 3; i++) {
        for (let j = y; j < y + 3; j++) {
            let value = board[i][j];
            if (value == num) {
                return false;
            }
        }
    }
    return true;
}

function checkRow(board, row, num) {
    for (let i = 0; i < board.length; i++) {
        let value = board[row][i];
        if (value == num) {
            return false;
        }
    }
    return true;
}

function checkCol(board, col, num) {
    for (let i = 0; i < board.length; i++) {
        let value = board[i][col];
        if (value == num) {
            return false;
        }
    }
    return true;
}

function isValid(board, row, col, num) {
    return checkRow(board, row, num) &&
        checkCol(board, col, num) &&
        checkSquare(board, row, col, num);
}

function solve(board) {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j] == ".") {
                for (let k = 1; k <= 9; k++) {
                    let num = k.toString();
                    if (isValid(board, i, j, num)) {
                        board[i][j] = num;
                        if (solve(board) == true) {
                            return true;
                        } else {
                            board[i][j] = ".";
                        }
                    }
                }
                return false;
            }
        }
    }
    return true;
}
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function (board) {
    solve(board);
    return board;
};

console.log(solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]));
["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
// [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
// console.log(solveSudoku());
// console.log(solveSudoku());
