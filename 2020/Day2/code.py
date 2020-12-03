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

def ParseLine(line):
    line = line.rsplit("-")
    minimum = int(line[0])
    line = line[1].rsplit(" ")
    maximum = int(line[0])
    character = line[1].rsplit(":")[0]
    password = line[2].strip()
    return minimum, maximum, character, password
    
def IsPasswordValidPartOne(line):
    minimum, maximum, character, password = ParseLine(line)
    count = password.count(character)
    if count >= minimum and count <= maximum:
        return 1
    else:
        return 0
        
def IsPasswordValidPartTwo(line):
    firstPos, secondPos, character, password = ParseLine(line)
    total = 0;
    if password[firstPos-1] == character:
        total += 1
    if password[secondPos-1] == character:
        total += 1
    if total == 1:
        return 1
    else:
        return 0

total = 0
for line in data:
    total += IsPasswordValidPartOne(line)
    
totalSecond = 0
for line in data:
    totalSecond += IsPasswordValidPartTwo(line)
    
print(total)
print(totalSecond)
