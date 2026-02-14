import itertools

def isQueenValid(pos):
    n = len(pos)

    for i in range(n):
        row1, col1 = pos[i]

        for j in range(i+1, n):
            row2, col2 = pos[j]
            if row1 == row2:
                return False

            if col1 == col2:
                return False

            if abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1: # Ini buat cek diagonal bersebelahan
                return False

    return True

def backtrack(index,colours, positions, queen):
    if index == len(colours):
        return True,0
    
    count = 0

    for pos in positions[index]:
        count += 1

        if isQueenValid(queen + [pos]):
            queen.append(pos)

            found, count1 = backtrack(index + 1, colours, positions, queen)
            count += count1

            if found:
                return True, count

            queen.pop()

    return False,count

def solveQueenPositions(area):
    orderedItems = list(area.items())
    orderedItems.sort(key=lambda x: len(x[1]))
    colours = [items[0] for items in orderedItems]
    positions = [list(items[1]) for items in orderedItems]
    queen = []
    found, count = backtrack(0, colours, positions, queen)
    if found :
        solution = {
            colours[i]: queen[i] for i in range (len(colours))
        }
        return True, solution, count
    return False, None, count