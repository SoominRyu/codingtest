a = []

for _ in range(5):
  a.append(list(input()))

lens = []
for i in range(5):
  lens.append(len(a[i]))

pr = ''
for i in range(max(lens)):
  for j in range(5):
    try:
      pr += a[j][i]
    except:
      continue
 

print(pr)