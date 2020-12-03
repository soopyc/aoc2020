f = open("input.txt", "r")
a = f.read()

i = a.split('\n')

x = 0
trees = 0
del i[0]
for b in i[1::2]:
  print(b)
  x = x + 1
  z = x % 31
  print(f'{x} and {z}')
  if b[z] == "#":
    trees = trees + 1




print(trees)

