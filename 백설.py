
from itertools import combinations


num = []
for _ in range(9):
  num.append(int(input()))

nan = list(combinations(num,7))

# print(nan)

for i in nan:
  if sum(i) == 100:
    for j in i:
      print(j)