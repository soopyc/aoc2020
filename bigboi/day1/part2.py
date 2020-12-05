f = open(r"2020/bigboi/day1/data1.txt", "r")
a = []

h = f.readlines()
print(len(h))
for i in h:
    a.append(int(i[0:len(i)-1]))
print(len(a))

for x in a:
    for y in a:
        for z in a:
            if (x+y+z == 2020):
                print(x*y*z)
