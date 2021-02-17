from statistics import mean
from scipy.stats import wilcoxon
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
enumArray= ["","Very slightly or not at all.","A little","Moderately","Quite a bit","Extremely"]
#enumurated = list(enumerate(enumArray, 1))
beforeOneArray = []
beforeTwoArray = []
afterOneArray = []
afterTwoArray = []
fileRead = open("WebsiteOneBefore.csv", "r")
lines = fileRead.readlines()
for line in lines:
    i = 0
    line = line[:-1]
    splitArray = line.split(',')
    for row in splitArray:
        row = row.strip("\"")
        if is_integer(row):
            splitArray[i] = int(row)
        elif row in enumArray:
            splitArray[i] = enumArray.index(row)
        i += 1
    beforeOneArray.append(splitArray)
fileRead = open("WebsiteOneAfter.csv", "r")
lines = fileRead.readlines()
for line in lines:
    i = 0
    line = line[:-1]
    splitArray = line.split(',')
    for row in splitArray:
        row = row.strip("\"")
        if is_integer(row):
            splitArray[i] = int(row)
        elif row in enumArray:
            print(row)
            splitArray[i] = enumArray.index(row)
            print(enumArray.index(row))
        i += 1
    afterOneArray.append(splitArray)
fileRead = open("WebsiteTwoBefore.csv", "r")
lines = fileRead.readlines()
for line in lines:
    i = 0
    line = line[:-1]
    builderArray = []
    splitArray = line.split(',')
    for row in splitArray:
        row = row.strip("\"")
        if is_integer(row):
            splitArray[i] = int(row)
        elif row in enumArray:
            splitArray[i] = enumArray.index(row)
        i += 1
    beforeTwoArray.append(splitArray)
fileRead = open("WebsiteTwoAfter.csv", "r")
lines = fileRead.readlines()
for line in lines:
    i = 0
    line = line[:-1]
    splitArray = line.split(',')
    for row in splitArray:
        row = row.strip("\"")
        if is_integer(row):
            splitArray[i] = int(row)
        elif row in enumArray:
            splitArray[i] = enumArray.index(row)
        i += 1
    afterTwoArray.append(splitArray)

beforeOneholder = beforeOneArray.pop(0)
afterOneHolder = afterOneArray.pop(0)
beforeTwoHolder = beforeTwoArray.pop(0)
afterTwoHolder = afterTwoArray.pop(0)
beforeOneScores = []
beforeTwoScores= []
j = 0
for line in beforeOneArray:
    i = 0
    individualArray = []
    for row in line:
        if i == 2 or i == 4 or i == 6 or i == 9 or i == 10 or i == 12 or i == 14 or i == 16 or i == 17 or i == 19:
            testnum = int(beforeOneArray[j][i])
            individualArray.append(testnum)
        elif i > 2:
            if beforeOneArray[j][i] == 5:
                individualArray.append(1)
            elif beforeOneArray[j][i] == 4:
                individualArray.append(2)
            elif beforeOneArray[j][i] == 3:
                individualArray.append(3)
            elif beforeOneArray[j][i] == 2:
                individualArray.append(4)
            elif beforeOneArray[j][i] == 1:
                individualArray.append(5)
        i += 1
    j += 1
    individualScore = mean(individualArray)
    beforeOneScores.append(individualScore)
j = 0
beforeTwoScores = []
for line in beforeTwoArray:
    i = 0
    individualArray = []
    for row in line:
        if i == 2 or i == 4 or i == 6 or i == 9 or i == 10 or i == 12 or i == 14 or i == 16 or i == 17 or i == 19:
            testnum = int(beforeTwoArray[j][i])
            individualArray.append(testnum)
        elif i > 2:
            if beforeTwoArray[j][i] == 5:
                individualArray.append(1)
            elif beforeTwoArray[j][i] == 4:
                individualArray.append(2)
            elif beforeTwoArray[j][i] == 3:
                individualArray.append(3)
            elif beforeTwoArray[j][i] == 2:
                individualArray.append(4)
            elif beforeTwoArray[j][i] == 1:
                individualArray.append(5)
        i += 1
    j += 1
    individualScore = mean(individualArray)
    beforeTwoScores.append(individualScore)
j = 0
afterOneScores = []
for line in afterOneArray:
    individualScore = 0
    individualArray = []
    i = 0
    for row in line:
        if i == 2 or i == 4 or i == 6 or i == 9 or i == 10 or i == 12 or i == 14 or i == 16 or i == 17 or i == 19:
            print("positive", afterOneArray[j][i])
            testnum = int(afterOneArray[j][i])
            individualArray.append(testnum)
        elif i > 2 and i < 22:
            print("negative", afterOneArray[j][i])
            if afterOneArray[j][i] == 5:
                individualArray.append(1)
            elif afterOneArray[j][i] == 4:
                individualArray.append(2)
            elif afterOneArray[j][i] == 3:
                individualArray.append(3)
            elif afterOneArray[j][i] == 2:
                individualArray.append(4)
            elif afterOneArray[j][i] == 1:
                individualArray.append(5)
        i += 1
    j += 1
    individualScore = mean(individualArray)
    afterOneScores.append(individualScore)
print(afterOneScores)
j = 0
afterTwoScores = []
for line in afterTwoArray:
    i = 0
    individualScore = 0
    individualArray = []
    for row in line:
        if i == 2 or i == 4 or i == 6 or i == 9 or i == 10 or i == 12 or i == 14 or i == 16 or i == 17 or i == 19:
            testnum = int(afterTwoArray[j][i])
            individualArray.append(testnum)
        elif i > 2 and i < 22:
            if afterTwoArray[j][i] == 5:
                individualArray.append(1)
            elif afterTwoArray[j][i] == 4:
                individualArray.append(2)
            elif afterTwoArray[j][i] == 3:
                individualArray.append(3)
            elif afterTwoArray[j][i] == 2:
                individualArray.append(4)
            elif afterTwoArray[j][i] == 1:
                individualArray.append(5)
        i += 1
    j += 1
    individualScore = mean(individualArray)
    afterTwoScores.append(individualScore)
print("Stats before one:", beforeOneScores)
print("Stats after one:", afterOneScores)
print("Stats before two:", beforeTwoScores)
print("Stats after two:",afterTwoScores)
