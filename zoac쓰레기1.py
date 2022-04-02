
a = list(input())

b = sorted(a)
print(b)
start = ord(b[0])
print(start)

for i in range(len(a)):
  ind = []
  for j in range(i+1):
    if start != a[-1]:
      rmin = ord(a[start+1])
      for s in range(start+1,-1):
        if ord(a[s]) < rmin:
          rmin = ord(a[s])
      


    print(a[j], end='')
  print("")