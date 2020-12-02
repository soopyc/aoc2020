def spl(word): 
  return [char for char in word]

f = open("input.txt", "r")
a = f.read()

b = a.split('\n')

valid = 0

for c in b:
  ifor = 0
  d = c.split(' ')
  minmax = d[0].split('-')
  min = int(minmax[0])-1
  max = int(minmax[1])-1
  character = d[1].replace(':', '')
  final = spl(d[2])
  if (final[min] == character):
    ifor = ifor + 1
  if (final[max] == character):
    ifor = ifor + 1
  if ifor == 1:
    valid = valid + 1
print(valid)
