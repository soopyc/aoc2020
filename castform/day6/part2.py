f = open(r"2020/bigboi/day6/data.txt" ,"r")
h = f.readlines()
f.close()
counter = 0
person = 0
dic = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0,'o':0, 'p':0, 'q':0,'r':0,'s':0,'t':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
for i in h:
    if i == "\n":
        for x in dic:
            if dic[x] == person:
                counter +=1
        
        person = 0
        dic ={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0,'o':0, 'p':0, 'q':0,'r':0,'s':0,'t':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    else:
        person +=1
        i = i.replace('\n', "")
        for x in i:
            dic[x] += 1
            
for x in dic:
    if dic[x] == person:
        counter +=1
print(counter)