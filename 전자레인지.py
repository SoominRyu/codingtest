t = int(input())

list1 = []

abc = [300,60,10]

for i in abc:
  list1.append(t//i)
  t = t - i*(t//i)

if t == 0:
  for k in list1:
    print(k,end=' ')
else:
  print(-1)