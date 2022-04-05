s = list(input())

sn = []

for i in range(len(s)):
  sn.append(''.join(s[i:]))

sn.sort()
for i in sn:
  print(i)