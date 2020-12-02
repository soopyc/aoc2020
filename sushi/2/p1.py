import re

def findOccurrences(s, ch):
  return [i for i, letter in enumerate(s) if letter == ch]

f = open("input.txt", "r")
a = f.read()

b = a.split('\n')

valid = 0

for c in b:
  d = c.split(' ')
  minmax = d[0].split('-')
  min = int(minmax[0])
  max = int(minmax[1])
  character = d[1].replace(':', '')
  final = d[2]
  instances = len(findOccurrences(final, character))
  if instances >= min and instances <= max:
    valid = valid + 1

print(valid)
