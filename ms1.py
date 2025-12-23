# board generation for mind sweaper 
import random

def createBoard(size:int, mines:int):
    board = [] #  [] []
    for i in range(size):
        board.append([0] * size)

    # print(board)
    i = 0
    minesSet = set()
    while i < mines:
        row = random.randint(0, mines - 1)
        col = random.randint(0, mines - 1)
        # print("r: %s c: %s val: %s" %(row, col, board[row][col]))
        if board[row][col] == 0:
            board[row][col] = "X"
            minesSet.add((row,col))
            i += 1
        # print(board)
        # break

    print(board)
    return board, minesSet

def getAdjacency(board, minesSet):
    n = len(board)
    m = len(board[0])
    for mine in minesSet: # (row,col)
        row, col = mine

        # 0, -1 left 
        # 1, -1 diagonal left up
        # -1, -1 diagonal left bottom

        # 0, 1 right
        # 1, 1 diagonal right up
        # -1, 1 diagonal right bottom

        # -1, 0 up
        # 1, 0 down

        for diag in range(-1, 2): # -1, 0, 1
            for d in range(-1, 2): # -1, 0, 1
                r = row + diag
                if r >= 0 and r < n and board[r][col] != "X":
                    board[r][col] += 1

                c = col + d 
                if c >= 0 and c < m and board[row][c] != "X":
                    board[row][c] += 1

    for row in board:
        line = ""
        for c in row:
            line += str(c) + " "
        print(line)            
        # print("\n")

board, mineSet = createBoard(10, 1)
getAdjacency(board, mineSet)