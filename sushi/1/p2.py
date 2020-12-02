sep = nums.splitlines()
for a in sep:
  for b in sep:
    for c in sep:
      a = int(a)
      b = int(b)
      c = int(c)
      if (a + b + c == 2020):
        print(a*b*c)
