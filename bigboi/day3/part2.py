f = open(r"2020/bigboi/day3/data.txt")
h = f.readlines()
f.close()

def findpath(h, ver, hori):
    place = 0
    counter = 0
    loop = 1
    h = h[1:]
    for i in h:
        i.replace("\n", "")
        if loop%ver == 0:
            place += hori
            if place > 30:
                place -= 31
            if i[place] == "#":
                counter +=1
        
        loop += 1
        
    return counter

a = findpath(h, 1, 1)
b = findpath(h, 1, 3)
c = findpath(h, 1, 5)
d = findpath(h, 1, 7)
e = findpath(h, 2, 1)
print(a*b*c*d*e)