f = open(r"2020/bigboi/day6/data.txt" ,"r")
h = f.readlines()
f.close()
tmpLet = []
counter = 0
for i in h:
    if i == "\n":
        counter += len(tmpLet)
        tmpLet = []
    else:
        i = i.replace('\n', "")
        for x in i:
            if x not in tmpLet:
                tmpLet.append(x)
counter += len(tmpLet)
print(counter)
