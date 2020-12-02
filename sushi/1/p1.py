sep = nums.splitlines()
for a in sep:
  for b in sep:
    a = int(a)
    b = int(b)
    if (a + b  == 2020):
      print(a*b)
