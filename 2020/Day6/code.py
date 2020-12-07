import os

filename = "data.txt"

def OpenInput(filename, mode = "r"):
    return open(filename, mode)
    
def GetPartOne(filename):
    total = 0
    group_answers = set()
    
    with OpenInput(filename) as in_file:
        for line in in_file.readlines():
            line = line.strip(os.linesep)
            if not line:
                #print(group_answers)
                total += len(group_answers)
                group_answers = set()
            else:
                for c in line:
                    group_answers.add(c)
    return total + len(group_answers)
    
def GetPartTwo(filename):
    total = 0
    group_answers = set()
    first_member = True
    
    with OpenInput(filename) as in_file:
        for line in in_file.readlines():
            line = line.strip(os.linesep)
            if not line:
                #print(group_answers)
                total += len(group_answers)
                group_answers = set()
                first_member = True
            elif first_member:
                for c in line:
                    group_answers.add(c)
                first_member = False
            else:
                individual_set = set()
                for c in line:
                    individual_set.add(c)
                group_answers = group_answers.intersection(individual_set)
    return total + len(group_answers)
    
    
print("Part One: sum is %d" % (GetPartOne(filename)))
print("Part Two: sum is %d" % (GetPartTwo(filename)))
