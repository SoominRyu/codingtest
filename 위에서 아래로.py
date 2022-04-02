n = int(input())
a = list()
for i in range(n):
  a.append(int(input()))

a.sort(reverse=True)

for i in range(n):
  print(a[i],end=' ')
