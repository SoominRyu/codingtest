while True:
  n = int(input())

  if n == 0:
    exit(0)
  s = []
  for i in range(n):
    s.append([input(),i])

  ss =[]

  for i in range(n):
    ss.append([s[i][0].lower(),s[i][1]])

  ss.sort()
  
  
  print(s[ss[0][1]][0])

