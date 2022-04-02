n = int(input())
count = 0
for _ in range(n):
  s = list(input())
  ss = set(s)

  if s == ss:
    count += 1
  else:
    sa = []
    for i in range(len(s)):
      if s[i] not in sa:
        sa.append(s[i])
      else:
        if s[i] != sa[-1]:
          break
      
      if i == len(s)-1:
        count += 1

print(count)
