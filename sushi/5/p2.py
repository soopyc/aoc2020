f = open("input.txt", "r")
a = f.read()
# [0:N] first
# [-N:] last
b = a.split('\n')
rowSeat = []
columnSeat = []
seatIDs = []
for c in b:
  rows = (list(range(0,128)))
  columns = (list(range(0,8)))
  x = c[0:7]
  y = c[-3:]
  for e in x: #first 7
    length = len(rows)
    middle_index = length//2
    first_half = rows[:middle_index]
    second_half = rows[middle_index:]
    if e == 'F':
      rows = first_half
    if e == 'B':
      rows = second_half
    if len(rows) == 1:
      rowSeat.append(rows[0])

  for e in y: #last 3
    length = len(columns)
    middle_index = length//2
    first_half = columns[:middle_index]
    second_half = columns[middle_index:]
    if e == 'L':
      columns = first_half
    if e == 'R':
      columns = second_half
    if len(columns) == 1:
      columnSeat.append(columns[0])
print(len(columnSeat))
print(len(rowSeat))
for i in range(0,846):
  rS = rowSeat[i]*8
  cS = columnSeat[i]
  seatIDs.append(rS+cS)
  seatIDs.sort()
for w in range(80,926):
  if w not in seatIDs:
    print(w)
  
