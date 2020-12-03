import os

def ReadInput(filename):
    File = open(filename, "r")
    return File

def InputToList(data):
    dataList = []
    for line in data:
        dataList.append(line.strip(os.linesep))
    return dataList
    
data = InputToList(ReadInput("data.txt"))
print(data)

def GetNextPosition(data, x, y, right, down):
    posX, posY = -1, -1
    if y + down < len(data):
        posY = y + down
        posX = (x + right) % len(data[0])
    return posX, posY
    

def CountTrees(data, right, down):
    treeCount = 0
    print(str(right) + ":" + str(down))
    x, y = GetNextPosition(data, 0, 0, right, down)
    while(y > 0):
        if data[y][x] == '#':
            treeCount += 1
        x, y = GetNextPosition(data, x, y, right, down)
    return treeCount
    
print("Part One : {} trees".format(CountTrees(data, 3, 1)))

total = 1
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for dx, dy in slopes:
    val = CountTrees(data, dx, dy)
    print(val)
    total *= val
    
print("Part Two : {} trees".format(total))
