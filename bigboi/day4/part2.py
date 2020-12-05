def byr(id):
    return (1920 <= int(id) <= 2002)

def iyr(id):
    return (2010 <= int(id) <= 2020)

def eyr(id):
    return (2020 <= int(id) <= 2030)

def hgt(id):
    if id[len(id)-2:] == 'cm':
        return (150 <= int(id[:len(id)-2]) <= 193)
    elif id[len(id)-2:] == 'in':
        return (59 <= int(id[:len(id)-2]) <= 76)
    else:
        return False

def hcl(id):
    if id[0] != '#':
        return False
    if len(id) != 7:
        False
    switch = {
        'a':True,
        'b':True,
        'c':True,
        'd':True,
        'e':True,
        'f':True,
        '0':True,
        '1':True,
        '2':True,
        '3':True,
        '4':True,
        '5':True,
        '6':True,
        '7':True,
        '8':True,
        '9':True
    }

    for i in id[1:]:
        if switch.get(i, False) == False:
            return False
    
    return True

def ecl(id):
    colors = ['amb','blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return id in colors

def pid(id):
    return (len(id) == 9)

def cid(id):
    return False

def validID(code, id):
    switch = {
        'byr':byr,
        'iyr':iyr,
        'eyr':eyr,
        'hgt':hgt,
        'hcl':hcl,
        'ecl':ecl,
        'pid':pid,
        'cid':cid
    }
    test = switch.get(code, lambda: "code1")
    return test(id)

f = open(r"2020/bigboi/day4/data.txt" ,"r")
h = f.readlines()
tmpWords = []
keys = 0
counter = 0
for i in h:
    if i == "\n":
        if keys == 7:
            counter += 1
        keys = 0
    else:
        i = i.replace("\n", "")
        tmpWords = i.split(" ")
        for a in tmpWords:
            code = a.split(':')
            if validID(code[0],code[1]) == True:
                keys += 1

if keys == 7:
    counter += 1
print(counter)
