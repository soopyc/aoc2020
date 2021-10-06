def findBinary(id, bin, plus):
    devider = (2**bin)
    total = 0
    for i in id:
        devider = devider//2 
        if i == plus:
            total += devider
    return total 

f = open(r"2020/bigboi/day5/data.txt" ,"r")
h = f.readlines()
f.close()
allIds = []

for i in h:
    i = i.replace('\n', "")
    row = i[:7]
    row = findBinary(row, len(row), 'B')
    column = i[7:]
    column = findBinary(column, len(column),'R')
    allIds.append(row*8 + column)

allIds.sort()
test = -2
for i in allIds:
    print(i - test)
    if i - test == 2:
        print(test + 1)
        break
    test = i