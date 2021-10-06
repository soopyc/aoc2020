f = open(r"2020/bigboi/day4/data.txt" ,"r")
h = f.readlines()
tmpWords = []
keys = 0
counter = 0
woah =0
for i in h:
    if i == "\n":
        woah += 1
        if keys == 7:
            counter += 1
        keys = 0
    else:
        tmpWords = i.split(" ")
        for a in tmpWords:
            if a[0:3] != "cid":
                keys += 1


print(counter)
