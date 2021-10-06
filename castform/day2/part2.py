counter = 0
test = 0
f = open(r"2020/bigboi/day2/data.txt")
h = f.readlines()
for i in h:
    lists = i.split(" ")
    lists[2] = lists[2].replace("\n", "")
    splits = lists[0].split("-")
    first = int(splits[0])-1
    second = int(splits[1])-1
    if (lists[2][first] == lists[1][0]):
        test +=1
    if (lists[2][second] == lists[1][0]):
        test +=1
    if (test == 1):
        counter +=1
    test = 0
print(counter)