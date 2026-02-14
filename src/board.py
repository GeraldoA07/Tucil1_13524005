import os 

def isBoardValid(n):
    if not (n):
        return False
    size = len(n)
    for line in n:
        if len(line) != size:
            return False
    return True

def groupColours(board):
    colours = {}
    n = len(board)
    for i in range(n):
        for j in range(n):
            colour = board[i][j]
            if colour not in colours:
                colours[colour] = []
            colours[colour].append((i, j))
    return colours


def printBoard(rows,solution):
    n = len(rows)
    board = [list(row) for row in rows]
    for pos in solution.values():
        row, col = pos
        board[row][col] = '#'
    for row in board:
        print(''.join(row))    