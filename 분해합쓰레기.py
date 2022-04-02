from itertools import permutations

n = list(input())
# nn = list(map(int,n))

p = list(permutations(range(0,10),len(n)))
# print(p)
num = []
for i in p:
  if i[0] <= int(n[0]):
    a = int(''.join(tuple(map(str,i))))
    if a <= int(''.join(n)):
      num.append(a)

# print(num)
# num.sort(reverse=True)
num = list(map(str,num))
# print(num)
for i in num:
  h = 0
  ii = list(i)
  # print(ii)
  for j in ii:
    h += int(j)
  # print(h+int(i))
  if int(i) + h == int(''.join(n)):
    print(int(i))
    exit(0)

print(0)