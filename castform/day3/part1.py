f = open(r"2020/bigboi/day3/data.txt")
h = f.readlines()
f.close()
#length of the string is 31!
#stop at 31
place = 0
counter = 0
h = h[1:]
for i in h:
    i.replace("\n", "")
    if place == 28:
        place = 0
    elif place == 29:
        place = 1
    elif place == 30:
        place = 2
    else:
        place += 3
    if i[place] == "#":
        counter +=1

print(counter)