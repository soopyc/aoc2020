p = a.split('\n\n')
valid = 0

for b in p:
  needed = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
  c = b.replace('\n', ' ').split(' ')
  for x in c:
    print(x)
    needed.remove(x[0:3])
  if (len(needed)) == 0 or needed[0] == 'cid':
    valid = valid + 1
print(valid)
