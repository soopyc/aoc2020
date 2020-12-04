f = open("input.txt", "r")
a = f.read()
import re

p = a.split('\n\n')
valid = 0

for b in p:
  needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
  c = b.replace('\n', ' ').split(' ')
  for x in c:
    r = x.split(':')
    g = r[0]
    z = r[1]
    #print(f'{g} and {z}')
    if g == 'byr': #good
      z = int(z)
      if z >= 1920 and z <= 2002:
        needed.remove(g)
    if g == 'iyr': #good
      z = int(z)
      if z >= 2010 and z <= 2020:
        needed.remove(g)
    if g == 'eyr':#good
      z = int(z)
      if z >= 2020 and z <= 2030:
        needed.remove(g)
    if g == 'hgt':
      u = int(re.search(r'\d+', z).group()) #int
      y = " ".join(re.findall("[a-zA-Z]+", z)) #cm/in
      if y == 'in':
        if u >= 59 and u <= 76:
          needed.remove(g)
      if y == 'cm':
        if u >= 150 and u <= 193:
          needed.remove(g)
    if g == 'hcl':
      f = 0
      t = z[1:]
      #print(t)
      for w in t:
        if w in ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']:
          f = f + 1
      if f == 6:
        #print(len(t))
        needed.remove(g)
    if g == 'ecl':
      if z in ['amb','blu','brn','grn','hzl','oth','gry']:
        needed.remove(g)
    if g == 'pid':
      if(len(z)) == 9:
        try:
          int(z)
          needed.remove(g)
        except:
          pass
       
  if (len(needed)) == 0 or needed[0] == 'cid':
    valid = valid + 1
print(valid)
