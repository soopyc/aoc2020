counter = 0
f = open(r"2020/bigboi/day2/data.txt")
h = f.readlines()
range1 = 0
range2 = 0
sums = 0
splits = []
for i in h:
    lists = i.split(" ")
    lists[2] = lists[2].replace("\n", "")
    splits = lists[0].split("-")
    sums = lists[2].count(lists[1][0])
    if (int(splits[0]) <= sums <= int(splits[1])):
        counter += 1
print(counter)