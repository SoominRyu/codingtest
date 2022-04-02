a = list(input())
# a.sort()
b = sorted(a)
# print(b)
for i in range(len(a)):
  ind = []
  for j in range(i+1):
    a_idx = a.index(b[j])
    if a_idx in ind:
      # print(a_idx)
      for s in range(a_idx+1,len(a)):
        # print("hel")
        if b[j] == a[s]:
          # print("hi")
          ind.append(s)
    else:
      ind.append(a.index(b[j]))
  # print(ind)
  ind.sort()
  # print(ind)
  for k in ind:
    print(a[k], end='')
  print("")