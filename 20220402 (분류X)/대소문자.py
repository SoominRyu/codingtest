s = list(input())
n = []
for i in s:
  if i.isupper() == True:
    n.append(i.lower())
  else:
    n.append(i.upper())

print(''.join(n))