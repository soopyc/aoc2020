def findBinary(id, bin, plus):
    devider = (2**bin)
    total = 0
    for i in id:
        devider = devider//2 
        if i == plus:
            total += devider
    return total 

def biggerId(row, column, old):
    id = row*8 + column
    if (id > old):
        return id
    else: 
        return old

f = open(r"2020/bigboi/day5/data.txt" ,"r")
h = f.readlines()
f.close()
highest = 0
for i in h:
    i = i.replace('\n', "")
    row = i[:7]
    row = findBinary(row, len(row), 'B')
    column = i[7:]
    column = findBinary(column, len(column),'R')
    highest = biggerId(row,column, highest)

print(highest)