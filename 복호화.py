n = int(input())

for _ in range(n):
  s = list(input().replace(' ',''))
  # print(s)
  c = []
  for i in s:
    c.append(s.count(i))
  
  m = c.index(max(c))
  # print(c,m)
  a = []
  for j in range(m,len(c)):
    if c[j] >= c[m]:
      a.append(s[j])
  
  a = set(a)
  # print(a)
  if len(a) == 1:
    print(s[c.index(max(c))])
  else:
    print("?")



  # print(s[c.index(max(c))])