import os

filename = "data.txt"

def OpenInput(filename, mode = "r"):
    return open(filename, mode)
    
def GetRow(line, rowMin, rowMax):
    c = line[0]
    diffRow = rowMax - rowMin
    delta = round(diffRow / 2)
    if c == 'F':
        if len(line) == 1:
            return rowMin
        else:
            return GetRow(line[1:], rowMin, rowMax - delta)
    elif c == 'B':
        if len(line) == 1:
            return rowMax
        else:
            return GetRow(line[1:], rowMin + delta, rowMax)
    else:
        print("Error: diffRow: %d / c: %s / line: %s" %(diffRow, c, line))
        
            
def GetColumn(line, colMin, colMax):
    c = line[0]
    diffCol = colMax - colMin
    delta = round(diffCol / 2)
    if c == 'L':
        if len(line) == 1:
            return colMin
        else:
            return GetColumn(line[1:], colMin, colMax - delta)
    elif c == 'R':
        if len(line) == 1:
            return colMax
        else:
            return GetColumn(line[1:], colMin + delta, colMax)
    else:
        print("Error: diffCol: %d / c: %s / line: %s" %(diffCol, c, line))
    
def GetSeatIDFromCode(line, rowMin, rowMax, colMin, colMax):
    row = int(GetRow(line[:-3], rowMin, rowMax))
    col = int(GetColumn(line[7:], colMin, colMax))
    return row * 8 + col
    
def GetSortedSeats(filename):
    seatIDs = []
    with OpenInput(filename) as in_file:
        for line in in_file.readlines():
            line = line.strip(os.linesep)
            seatIDs.append(GetSeatIDFromCode(line, 0, 127, 0, 7))
    seatIDs.sort()
    return seatIDs

def FindMissingSeat(seats):
    for i in range(1, len(seats) - 1):
        if seats[i] - 1 != seats[i-1]:
            return seats[i]-1
        if seats[i] + 1 != seats[i+1]:
            return seats[i]+1
    return -1

seats = GetSortedSeats(filename)
print("Part one : highest seat ID %d " % seats[-1])
print("Part two : missing seat ID %d " % FindMissingSeat(seats))