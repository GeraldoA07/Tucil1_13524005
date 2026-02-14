import os
from PIL import Image, ImageDraw

base = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
palette = [
    "#C6E0B4", "#FFE699", "#A9D18E", "#F4B6B6", "#9DC3E6",
    "#B4A7D6", "#D996B6", "#F9CB9C", "#A2C4C9", "#D9D9D9",
    "#93C47D", "#FFD966", "#6FA8DC", "#E06666", "#8E7CC3",
    "#C27BA0", "#F6B26B", "#76A5AF", "#B7B7B7", "#B6D7A8",
]
queenImg = os.path.join(base, "assets", "crown.png")

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


def saveImage(board, solution, path):
    crown = Image.open(queenImg).convert("RGBA")

    n = len(board)
    cell = max(20, min(48, 600 // max(1, n)))
    size = n * cell

    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    colourMap = {}
    queens = set(solution.values())

    def color(ch):
        key = ch.upper()
        if key not in colourMap:
            colourMap[key] = palette[len(colourMap) % len(palette)]
        return colourMap[key]

    sizeCrown = int(cell * 0.7)
    crownResize = crown.resize((sizeCrown, sizeCrown), Image.LANCZOS)
    
    for r in range(n):
        for c in range(n):
            x1, y1 = c * cell, r * cell
            x2, y2 = x1 + cell, y1 + cell
            fill = color(board[r][c])
            draw.rectangle([x1, y1, x2, y2], fill=fill, outline="#222", width=2)
            if (r, c) in queens:
                if crownResize:
                    cx = int(x1 + (cell - crownResize.width) / 2)
                    cy = int(y1 + (cell - crownResize.height) / 2)
                    img.paste(crownResize, (cx, cy), crownResize)
                else:
                    draw.text((x1 + cell * 0.35, y1 + cell * 0.2), "#", fill="#111")

    img.save(path)
    return True
    