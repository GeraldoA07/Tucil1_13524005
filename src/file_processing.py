import os

def readBoard(filePath):
    file = open(filePath, "r")
    lines = []

    for line in file:
        line = line.strip()
        if line != '':
            lines.append(line)
    file.close()
    return lines

def saveSolution(path, oriBoard, solution, time, count):
    board = [list(row) for row in oriBoard]
    
    for pos in solution.values():
        row, col = pos
        board[row][col] = '#'
        
    f = open(path,'w')
    for row in board:
        f.write(''.join(row) + '\n')
        
    f.write(f"\nWaktu eksekusi: {time} ms\n")
    f.write(f"Banyak kasus yang ditinjau: {count} kasus\n")
    f.close()
    