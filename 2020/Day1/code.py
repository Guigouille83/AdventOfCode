import os

def ReadInput(filename):
    File = open(filename, "r")
    return File

def InputToList(data):
    dataList = []
    for line in data:
        dataList.append(int(line.strip(os.linesep)))
    return dataList

def FindResultPartOne(data, sumTotal):
    result = 0
    for x in data:
        val = sumTotal - x
        if val in data:
            result = x * val
            break
    return result

def FindResultPartTwo(data, sumTotal):
    result = 0
    for x in data:
        xIndex = data.index(x)
        val = FindResultPartOne(data[xIndex:], sumTotal - x)
        if val != 0:
            result = val * x
    return result
    
data = InputToList(ReadInput("data.txt"))

print(FindResultPartOne(data, 2020))
print(FindResultPartTwo(data, 2020))
